'''
Created on May 14, 2017

@author: rezakhoshkangini
'''
import os
import traceback
import weka.core.jvm as jvm
import wekaexamples.helper as helper
from weka.core.converters import Loader
from weka.classifiers import Classifier, SingleClassifierEnhancer, MultipleClassifiersCombiner
#from weka.classifiers import FilteredClassifier, PredictionOutput, Kernel, KernelClassifier
from weka.classifiers import Evaluation
from weka.filters import Filter
from weka.core.classes import Random
import weka.plot.classifiers as plot_cls
import weka.plot.graph as plot_graph
#import weka.core.types as types


class  classifier_data(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.arffInput()
    
    def arffInput(self):
         # load a dataset
        iris_file = helper.get_data_dir() + os.sep + "/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/Section0.arff"
        helper.print_info("Loading dataset: " + iris_file)
        loader = Loader("weka.core.converters.ArffLoader")
        iris_data = loader.load_file(iris_file)
        iris_data.class_is_last()
    # classifier help
        helper.print_title("Creating help string")
        classifier = Classifier(classname="weka.classifiers.trees.J48")
        print(classifier.to_help())
        
        # build a classifier and output model
    helper.print_title("Training J48 classifier on iris")
    classifier = Classifier(classname="weka.classifiers.trees.J48")
    # Instead of using 'options=["-C", "0.3"]' in the constructor, we can also set the "confidenceFactor"
    # property of the J48 classifier itself. However, being of type float rather than double, we need
    # to convert it to the correct type first using the double_to_float function:
 #   classifier.set_property("confidenceFactor", types.double_to_float(0.3))
 #   classifier.build_classifier(iris_data)
    print(classifier)
    print(classifier.graph)
    plot_graph.plot_dot_graph(classifier.graph)