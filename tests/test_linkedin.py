import sys
import os
import csv

# Pega o caminho da pasta atual e adiciona a pasta "pai" (..) ao sistema de busca do Python
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_pai = os.path.join(diretorio_atual, '..')
sys.path.insert(0, diretorio_pai)

from main import main as linkedin_extractor

def test_linkedin():
    jobs_list = linkedin_extractor()
                    
    assert len(jobs_list) > 0
        