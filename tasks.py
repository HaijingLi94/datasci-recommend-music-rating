import d6tflow
import luigi
import pandas as pd

import cfg

class TaskGetData(d6tflow.tasks.TaskPqPandas):
    persist = ['train','words','users']

    def run(self):
        df_train = pd.read_csv('data/train.csv')
        df_users = pd.read_csv('data/users.csv')
        df_words = pd.read_csv('data/words.csv')
        self.save({'train':df_train,'words':df_words,'users':df_users})

@d6tflow.requires(TaskGetData)
class TaskPreprocess(d6tflow.tasks.TaskPqPandas):

    def run(self):
        df_train, df_users, df_words = self.inputLoad()

        df_train = df_train.merge(df_users, on=['Artist', 'User'])
        df_train = df_train.merge(df_words, left_on=['User'], right_on='RESPID')
        df_train['target']=df_train['Rating']

        self.save(df_train)

