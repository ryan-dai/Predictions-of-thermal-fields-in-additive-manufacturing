# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:17:26 2020

@author: Kari Ness
"""
import os 
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pathlib import Path

class Material:
    def __init__(self,material_properties, material_name):
        #The material_properties should be a list of strings containing material property types
        self.material_properties = material_properties
        
        #The material should be a string
        self.material_name = material_name
        
    def get_material_name(self):
        return self.material_name
        
    def get_path_string(self):
        material_name = self.get_material_name()
        p = Path('../Materials/' + material_name)
        return p.resolve()
    
    def get_property_file_path(self, material_property):
        material_name = self.get_material_name()
        file_name = material_name + '_' + material_property + '.txt'
        file = Path('../Materials/' + material_name + '/' + file_name)
        return file.resolve()
    
    def get_property_table(self, material_property):
        file_path = str(self.get_property_file_path(material_property)).replace('/','//')
        table = []
        with open(file_path,"r") as f:
            for line in f:
                tmp = line.strip().split(",")
                for i in range(0,len(tmp)):
                    tmp[i] = float(tmp[i])
                tmp = tuple(tmp)
                table.append(tmp)
        return table
    
    def plot_conductivity(self):
        material_name = self.get_material_name()
        degree_sign= u'\N{DEGREE SIGN}'
        table_conductivity = self.get_property_table('Conductivity')
        temp = [x[0] for x in table_conductivity]
        conductivity = [x[1] for x in table_conductivity]
        mpl.style.use('seaborn-dark-palette')
        plt.plot(conductivity, temp, c= 'firebrick')
        plt.xlabel('Temperature [C' + degree_sign + ']')
        plt.ylabel('Conductivity [W/m' + degree_sign + 'C]')
        path = str(self.get_path_string()) + '/'
        plt.savefig(path + '/' + material_name + '_Conductivity.png')
        plt.show()
        
    def plot_specific_heat(self):
        mpl.style.use('seaborn-dark-palette')
        degree_sign= u'\N{DEGREE SIGN}'
        material_name = self.get_material_name()
        table_specific = self.get_property_table('SpecificHeat')
        temp = [x[0] for x in table_specific]
        specific_heat = [x[1] for x in table_specific]
        plt.plot(specific_heat, temp, c='firebrick')
        plt.xlabel('Temperature [C' + degree_sign + ']')
        plt.ylabel("Specific heat [J/kg" + degree_sign + 'C]')
        path = str(self.get_path_string()) + '/'
        plt.savefig(path + '/' + material_name + '_SpecificHeat.png')
        plt.show()
        
    def plot_yield_stress(self):
        mpl.style.use('seaborn-dark-palette')
        degree_sign= u'\N{DEGREE SIGN}'
        material_name = self.get_material_name()
        table_yield = self.get_property_table('Plastic')
        plastic_strain = [x[1] for x in table_yield]
        yield_stress_tmp = [x[0] for x in table_yield]
        temp_tmp = [x[2] for x in table_yield]
        yield_stress = []
        temp = []
        for i in range(0,len(plastic_strain)):
            if plastic_strain[i] != 0:
                temp.append(temp_tmp[i])
                yield_stress.append(yield_stress_tmp[i])
        plt.plot(temp, yield_stress,c='firebrick')
        plt.xlabel('Temperature [C' + degree_sign + ']')
        plt.ylabel("Yield stress [MPa]")
        path = str(self.get_path_string()) + '/'
        plt.savefig(path +  '/' + material_name + '_Yield_Stress.png')
        plt.show()
        
    def plot_youngs_module(self):
        mpl.style.use('seaborn-dark-palette')
        degree_sign= u'\N{DEGREE SIGN}'
        material_name = self.get_material_name()
        table_E = self.get_property_table('Elastic')
        E = [x[0] for x in table_E]
        temp = [x[2] for x in table_E]
        plt.plot(temp,E, c='firebrick')
        plt.xlabel('Temperature [C' + degree_sign + ']')
        plt.ylabel("Young's Modulus [GPa]")
        path = str(self.get_path_string()) + '/'
        plt.savefig(path + '/' + material_name + '_Elastic.png')
        plt.show()
        
    def plot_expansion(self):
        mpl.style.use('seaborn-dark-palette')
        degree_sign = u'\N{DEGREE SIGN}'
        alpha_sign = '\u03B1'
        material_name = self.get_material_name()
        table_exp = self.get_property_table('Expansion')
        alpha = [x[1]*10**(6) for x in table_exp]
        T = [x[0] for x in table_exp]
        plt.plot(T,alpha, c='firebrick')
        plt.xlabel('Temperature [C' + degree_sign + ']')
        plt.ylabel(alpha_sign + 'x10^-6[1/' + degree_sign + 'C]')
        path = str(self.get_path_string()) + '/'
        plt.savefig(path + '/' + material_name + '_Expansion.png')
        plt.show()
        
    def material_plot(self):
        self.plot_conductivity()
        self.plot_yield_stress()
        self.plot_specific_heat()
        self.plot_youngs_module()
        self.plot_expansion()
