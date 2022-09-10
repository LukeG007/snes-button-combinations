import sys
import os

class CombinationMGMT:
    def __init__(self):
        sys.path.insert(0, 'combinations')
        combinations_dir_list = os.listdir('combinations')
        self.loaded_combinations = []
        for file in combinations_dir_list:
            if file.endswith('.py'):
                self.loaded_combinations.append(__import__(file.replace('.py', ''), fromlist=['']).Combination())
        
    def check_combination(self, read):
        for combination in self.loaded_combinations:
            combination_fields = []
            for field in combination.combo:
                combination_fields.append(field)
            
            failed = False
            for field in combination_fields:
                if not read[field] == combination.combo[field]:
                    failed = True
            
            if not failed:
                combination.callback()
