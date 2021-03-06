'''
Created on 28 sep. 2011

@author: localadmin
'''
from expWorkbench import ParameterUncertainty, Outcome, ModelEnsemble,\
                         ema_logging, ModelStructureInterface

class ParallelTestEMA(ModelStructureInterface):
    '''
    This class represents a simple example of how one can extent the basic
    ModelStructureInterface in order to do EMA on a simple model coded in
    Python directly
    '''
    
    #specify uncertainties
    uncertainties = [ParameterUncertainty((0.1, 10), "x1"),
                    ParameterUncertainty((-0.01,0.01), "x2"),
                    ParameterUncertainty((-0.01,0.01), "x3")]
    
    #specify outcomes 
    outcomes = [Outcome('y', time=False)]
    
    def model_init(self, policy, kwargs):
        pass
    
    def run_model(self, case):
        """Method for running an instantiated model structure """
        self.output[self.outcomes[0].name] =  case['x1']*case['x2']+case['x3']
        ema_logging.info("run model called")


if __name__ == '__main__':
    ema_logging.log_to_stderr(ema_logging.INFO)
    
    model = ParallelTestEMA(None, 'simpleModel') 
    ensemble = ModelEnsemble() 
    ensemble.set_model_structure(model) 
    ensemble.parallel = True
    results = ensemble.perform_experiments(201) 