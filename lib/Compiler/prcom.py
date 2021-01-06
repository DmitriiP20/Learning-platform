import f_functionclass.py as Functions
import g_graphclass.py as Graphs
import g_geometricObjects as Geometric

class compiler(object):

	raw_source_text = None	#Raw text file content
	proc_source_text = None #Dictionary of 3 Texts; Params, Statement and Conf
	statement = None 	#Raw Statement
	params = None 	#Dictionary of statement 
	configs = None	#Dictionary of Configurations 
	context = None	#Dictionary of Context

	Functions_List = None	#List of functions 
	Graphs_List = None 		#List of Graphs 

	def __init__(self, file, context):
		self.file = file
		self.context = context

	######################Text Loading and Processing################

	def load_source_text(self):
		fp = open(self.file, 'r')

		source_text = fp.readlines()


		for i in range(len(source_text)):
			source_text[i] = source_text[i].replace('\n','')
			source_text[i] = source_text[i].replace('\t','')

		self.raw_source_text = source_text

		fp.close()
	#This code is pretty bad
	def process_source_text(self):
		i = 0
		params = []
		statement = []
		config = []

		while(self.raw_source_text[i].replace(' ', '') != '---'):
			params.append(self.raw_source_text[i])
			i = i+1

		i = i+1
		while(self.raw_source_text[i].replace(' ', '') != '---'):
			statement.append(self.raw_source_text[i])
			i = i+1

		i = i+1
		while(self.raw_source_text[i].replace(' ', '') != '---'):
			config.append(self.raw_source_text[i])
			i = i+1

		self.proc_source_text = {"params":params, "statement":statement, "config":config};

		


	#####################Extraction from Text########################


	#This should be implemented right after we implement the configuration and initiation logic.
	#Once that is done, it should be obvious what we need to extract, and in what format.
	
	def get_statement(self):
		self.statement = self.proc_source_text['statement']

	def get_params(self):
		param_text = self.proc_source_text['params']
		params = {}

		for line in param_text:
			if ":" in line:
 				l = line.split(':')
 				params[l[0]] = l[1]

		self.params = params
 

	def get_config(self):
		pass


	def get_components(self):
		self.get_statement()
		self.get_config()
		self.get_statement()


	#######################Initiate Objects########################## 

	def resolve_function_from_context(self,f):
		#This function takes a function name, and find the corresponding expression in the context.
		#return the expressuin
		pass



	#For the the following two functions, we need to decide how we will represent functions and graphs in the Functions_List and Graphs_List.
	#I was thinking of storing them as pairs of names and functions objs.
	def make_function(self,f_name,expr):

		pass

	def make_graph(self,g_name):
		pass




	def init_functions(self):
		
		functions_names = self.params['Functions'] #List of function names

		for f in functions_names:
			f_expr = self.resolve_function_from_context(f)
			self.Functions_List.append(self.make_function(f,f_expr))
		
	def init_graphs(self):
		graphs_names = self.params['Graphs']
		for g in graph_names:
			self.Graphs_List.append(self.make_graph(g))

	def init_objs(self):
		self.init_functions()
		self.init_graphs()

	########################Configure Objects##########################
	def config_functions(self):
		pass



	############Graph Configuration###############
	
	def parse_config(self,config_type,config_statement):
		#this will be a big finction, it takes the config 
		#type, i.e. Functions. points, Interval...etc, and 
		#the exact config statement, and parse it, so that it 
		#is ready to be used to configure a graph object.
		#Returns a Dictionary of the form {config_type:parsed_config}
		pass 

	def get_graph_config(self,graph):
		#Takes the configuration dictionary we extracted from text,
		#extracts the graph configuration, then loops through it
		#parsing any configuration statment.

		#returns a configuration dictionary with the same keys but parsed statemtns
		graph_config = {}
		for key, value in self.config[graph].items():
			graph_config[key] = self.parse_config(key,value)

		return graph_config

	

	#For the following methods, we might want to change the graph class in the backend! 		
	def graph_interval(self,graph,graph_config):
		return graph_config['Interval']

	def graph_functions(self,graph,graph_config, Interval):
		functions = graph_config['Functions']
		graph.make_graphs(functions, Interval)
		

	def graph_points(self,graph,graph_config):
		points = graph_config['Points']
		graph.plot_points(points)

	def graph_axis(self,graph,graph_config):
		pass

	def config_graphs(self):
		for g in self.Graphs_List:
			g_config = self.get_graph_config(g)
			Interval = self.graph_interval(g,g_config)
			self.graph_functions(g,g_config,Interval)
			self.graph_points(g,g_config)
			self.graph_axis(g,g_config)




##########################################################
	def config_objs(self):
		self.config_functions()
		self.config_graphs()

	



	########################Fill Statement###############################
	def resolve_variables(self):
		pass

	def Parse_Statement(self):
		pass

	def make_graphs(self):
		pass

	def fill_statement(self):
		self.resolve_variables()
		self.Parse_Statement()
		self.make_graphs()

	

	######################Generate Problem Obj or Jupyter#################

	def generate_problem(self):
		pass	



	def compile(self):
		self.get_components()
		self.init_objs()
		self.config_objs()
		self.fill_statement()
		self.generate_problem()


