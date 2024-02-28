import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from pulp import *
from tabulate import tabulate
import time


def local_section_generator(bounds):
    '''
    Transform the structure of bounds for later algorithm implementation.
    '''
    max = []
    min = []
    for i in range(len(bounds)):
        max.append(bounds[i][1])
        min.append(bounds[i][0])
    return [min, max]


def find_leaves(node_id, tree_):
    '''
    return all leaves of a specific node in list form.
    '''
    if tree_.children_left[node_id] == -1:
        return [node_id]
    else:
        return find_leaves(tree_.children_left[node_id], tree_) + find_leaves(tree_.children_right[node_id], tree_)


class RF:
    """
    Random Forest Surrogate. Based on sklearn.ensemble.RandomForestRegressor
    """
    model = None
    optimizedParameter = None
    scoring = None
    bounds = []
    types = None
    output = None
    MIP = None
    ParameterName = None
    Features = None
    Labels = None


    def __init__(self, parameterInfo, scoring="neg_mean_squared_error"):
        """
        Initialize a Random Forest surrogate.
        :param parameterInfo: A Pandas Dataframe. Default = None
            A dataframe containing information of your input variables. It should contain four columns: Name, lb, ub
            and types, which correspond to the names, lower bounds, upper bounds and types of your input variables.
            You can find an example by checking "example.xlsx" in https://github.com/Shawn1eo/pyISBO.
        :param scoring: A string or callable object. Default = "neg_mean_squared_error"
            You can name a specific scoring metric for the surrogate. Use sorted(sklearn.metrics.SCORERS.keys()) to
            get valid options.
        """
        self.scoring = scoring
        for i in range(parameterInfo.shape[0]):
            self.bounds.append((parameterInfo["lb"][i], parameterInfo["ub"][i]))
        self.ParameterName = list(parameterInfo.pop("parameterName"))
        self.types = list(parameterInfo.pop("type"))
        self.types = [LpContinuous if self.types[i] == "Continuous" else LpInteger for i in range(len(self.types))]
    
    def _fit_text_output(self,errorMode,value):
        error = [['Model','Random Forest Regressor'],[errorMode,value]]
        table = tabulate(error, tablefmt='grid')
        return table

    def fit(self, X, y, n_estimators = 100, criterion = "squared_error", max_depth = None, min_samples_split = 2, min_samples_leaf = 1,bootstrap = True):
        """
        Fit Random Forest model.
        :param X:{array-like, sparse matrix} of shape (n_samples, n_features)T
            Training data.
        :param y:array-like of shape (n_samples,) or (n_samples, n_targets)
            Target values. Will be cast to X's dtype if necessary.
        :return: A float number.
            The cross-validation score of the fitted model based on the scoring metric you choose.
        """
        print("Now fitting Random Forest.")
        if(min_samples_split == 2):
            min_samples_split = round(0.02*len(X))
        model = RandomForestRegressor(n_estimators = n_estimators, criterion = criterion, max_depth = max_depth, 
                                      min_samples_split = min_samples_split, min_samples_leaf = min_samples_leaf,
                                      bootstrap = bootstrap)  # 实例化
        self.Features = X
        self.Labels = y
        model.fit(X, y)
        score = np.mean(cross_val_score(model, X, y, cv=5, scoring=self.scoring))
        self.model = model
        output_text = self._fit_text_output(self.scoring,score)
        print(output_text)
        return None

    def predict(self, X):
        """
        Predict using the surrogate.
        :param X:{array-like, sparse matrix} of shape (n_samples, n_features)T
            Training data.
        :return:An array, shape (n_samples,)
            Predicted values.
        """
        return self.model.predict(X)
    
    def _objective_set(self, y, func = None):
        y = y.flatten()
        if func == None:
            return(y[0])
        else:    
            return func(y)

    def MIP_transform(self,func = None):
        """
        Transform the surrogate into a Pulp mix integer program
        :return: None.
        """
        MIP = LpProblem("random_forest", LpMinimize)
        estimators_ = self.model.estimators_

        leaves_num = []
        for i in range(len(estimators_)):
            leaves_num.append(find_leaves(0, estimators_[i].tree_))
        x_len = len(self.types)
        local_section = local_section_generator(self.bounds)
        x_variable = {}

        '''
        Adding variables:
            Each input parameter corresponds to a variable (x_variable).
            Each leaf node corresponds to a binary variable (y_variable).
        '''
        for i in range(x_len):
            x_variable[i] = LpVariable('x_{}'.format(i), lowBound=local_section[0][i], upBound=local_section[1][i],
                                          cat=self.types[i])

        y_variable = {}
        for j in range(len(estimators_)):
            y_variable[j] = LpVariable.dict('y_{}'.format(j), range(len(leaves_num[j])), cat=LpBinary)

        '''
        Setting a dictionary: with the effect of finding the corresponding decision
        variable by the index of the leaf node.
        '''
        y_dict_list = []
        for j in range(len(estimators_)):
            y_dict = {}
            for i in range(len(leaves_num[j])):
                y_dict[leaves_num[j][i]] = y_variable[j][i]
            y_dict_list.append(y_dict.copy())

        '''
        Set objective function.
        '''
        objective = 0
        for j in range(len(estimators_)):
            objective += lpSum(
                y_variable[j][i] * self._objective_set(estimators_[j].tree_.value[leaves_num[j][i]],func) for i in range(len(leaves_num[j])))
        MIP += objective

        '''
        Adding constraints: 
            Each branch node corresponds to two constraints;
            Only one of all leaf nodes can be selected.
        '''
        # Note that since pulp does not allow large numbers with high
        # precision, float(inf) is not allowed.
        M = 10000
        for m in range(len(estimators_)):
            for i in range(estimators_[m].tree_.node_count):
                if estimators_[m].tree_.children_left[i] != -1:
                    cons_leaves_1 = find_leaves(estimators_[m].tree_.children_left[i], estimators_[m].tree_)
                    MIP += M * (lpSum(y_dict_list[m][j] for j in cons_leaves_1) - 1) - (
                                estimators_[m].tree_.threshold[i] - x_variable[estimators_[m].tree_.feature[i]]) <= 0,\
                           "tree_{}_node_{}_left".format(m,i)
                    cons_leaves_2 = find_leaves(estimators_[m].tree_.children_right[i], estimators_[m].tree_)
                    MIP += M * (lpSum(y_dict_list[m][j] for j in cons_leaves_2) - 1) + (
                                estimators_[m].tree_.threshold[i] - x_variable[
                            estimators_[m].tree_.feature[i]]) + 1 / M <= 0, \
                           "tree_{}_node_{}_right".format(m,i)
            MIP += lpSum(y_variable[m][i] for i in range(len(y_variable[m]))) == 1, "tree_{}_leaf".format(m)
        for i in range(x_len):
            MIP += x_variable[i] >= local_section[0][i], "x_lb_{}".format(i)
            MIP += x_variable[i] <= local_section[1][i], "x_ub_{}".format(i)
        self.MIP = MIP
    
    def _optimize_text_output(self,solve_time):
        head = ['MODEL',"random forest"]
        status = ['STATUS',LpStatus[self.MIP.status]]
        solve = ['SOLVING TIME','{} secs'.format(solve_time)] 
        value = ['OPTIMAL VALUE',round(self.output,7)]
        table = [head,status,solve,value]
        for i in range(len(self.types)):
            table.append([self.ParameterName[i],self.optimizedParameter[i]])
        table = tabulate(table,tablefmt='grid')
        return table
        
    def optimize(self,timeLimit=None):
        """
        solve the Pulp mix integer program
        :return: None.
        """
        if self.MIP is None:
            self.MIP_transform()

        start_time = time.time()
        self.MIP.solve(GLPK_CMD(msg=1, timeLimit=timeLimit))
        end_time = time.time()
        solve_time = round(end_time - start_time,3)
        self.optimizedParameter = [self.MIP.variablesDict()["x_%d" % i].varValue for i in range(len(self.types))]
        # The objective function of the random forest is to sum the values of
        # all trees, averaging on return to maintain consistency with y.
        self.output = value(self.MIP.objective) / len(self.model.estimators_)
        output_text = self._optimize_text_output(solve_time)
        print(output_text)
    
    def update(self,X,y,UpdateMode,Reprocess = True):
        if UpdateMode == 'w':
            self.Features = X
            self.Labels = y
        elif UpdateMode == 'a':
            self.Features = self.Features.append(X,ignore_index=True)
            self.Labels = self.Labels.append(y,ignore_index=True)
        else:
            print("Input must be 'a' or 'w'.")
            return None
        if Reprocess:
            self.fit(self.Features,self.Labels)
            self.optimize()



if __name__ == "__main__":
    import pandas as pd
    def sumfunc(y):
        return(y[0]+y[1])
    # data = pd.read_excel("Example.xlsx")
    # Output = data['target'].copy()
    # print(Output.head(5))
    # data = data.drop(["target"],axis = 1)
    # type = np.full(data.shape[1],'Continuous')
    # lb = np.min(data,axis = 0)
    # ub = np.max(data,axis = 0)
    # ParameterInfo = pd.DataFrame({'type':type,'lb':lb,'ub':ub})
    data = pd.read_excel("Example.xlsx")
    ParameterInfo = pd.read_excel("Example.xlsx", 1)
    y = data.pop("y")
    y_c = y.copy()**2
    y = pd.DataFrame({'y1':y,'y2':y_c})
    new_X = data.head(5)
    new_y = y.head(5)
    print(y.head(5))
    # model = AutoRegression(2, ParameterInfo)
    # model.fit(data, Output)
    # model.optimize("MAXIMIZE")

    m = RF(ParameterInfo, "r2")
    m.fit(data, y)
    m.MIP_transform(func = sumfunc)
    m.optimize(timeLimit=300)

    m.update(new_X,new_y,UpdateMode='a')