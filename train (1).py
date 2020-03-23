

from azureml.core import Run

run = Run.get_context() 

#Log a metric value. This is logged as a scalar to the 'Metrics' tab
run.log('Accuracy', 4)

#log an image to a run. This is of type Image and is logged under the 'Outputs + logs' tab and can be found in the 'logs' folder
run.log_image('food', path='./breadpudding.jpg', plot=None, description='food is life')

#log list of values to a run. This is logged as a 'Vector' and can be found under the 'Metrics' tab *the chart is off and the index looks strange. 
#x axis is 'Index'
my_list1 = ['a', 'b', 'c']
my_list2 = [1, 2, 3]
run.log_list('Letters', value=my_list1, description='some letters')
run.log_list('Numbers', value=my_list2, description='some numbers')

#log a row to a run. This is logged as type 'Table' and is found under the 'Metrics' tab
citrus = ['orange', 'lemon', 'lime'] 
sizes = [ 10, 7, 3] #y axis

#x axis is fruit
#y axis is sizes 
    
for index in range(len(citrus)):
    run.log_row("citrus", fruit = citrus[index], size=sizes[index])


#log a table to a run. This is logged as type 'Table' and is found under the 'Metrics' tab and under the 'Table' option. First value(keys) is the column name  

fruits = dict([('apples', '5'), ('pears', '9'), ('oranges', '7'), ('bananas', '4'), ('plums', '2') ])
run.log_table('test table', fruits, description='testing table')

#log confusion matrix to an AML run. This is logged as a confusion_matrix type and can be found under the 'Outputs + logs' tab and can be found in the 'logs' folder
# More info - https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html 

from sklearn.metrics import confusion_matrix
from azureml.core import Run

run = Run.get_context()

y_true = ["cat", "dog", "cat", "cat", "dog", "fish"]
y_pred = ["dog", "dog", "cat", "cat", "dog", "cat"]
matrix = confusion_matrix(y_true, y_pred, labels=["dog", "fish", "cat"])

run.log_confusion_matrix(name='confusion_matrix', 
                         value={
                           "schema_type": "confusion_matrix",
                           "schema_version": "v1",
                           "data": { 
                               "class_labels": ["dog", "fish", "cat"], 
                               "matrix": matrix.tolist() 
                           }
                         })



