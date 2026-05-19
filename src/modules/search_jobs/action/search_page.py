
from src.shared.navigation import Navigation
from src.modules.search_jobs.common.selectors import selectors
from src.shared.contants.urls import JOBS_URL
import csv
import os

class JobsPage:
    def __init__(self, navigation: Navigation):
        self.navigation = navigation
    
    def search_jobs(self, job_name="RPA"):
        self.navigation.goto_url(JOBS_URL + f"search-results/?keywords={job_name}")
        jobs = self.navigation.wait_get_element('//div[@data-component-type="LazyColumn"]//div[@role="button" and @tabindex=0]')
        
        list_jobs = []
        for job in jobs.all():
            job.click()
            column_infos = self.navigation.wait_get_element('//div[@data-component-type="LazyColumn"]//p//a')
            infos = column_infos.all_inner_texts()
            list_jobs.append({
                "company": infos[0],
                "job_title": infos[1]
            })
            
        self._save_jobs_in_csv(list_jobs=list_jobs)

    def _save_jobs_in_csv(self,list_jobs):
        nome_arquivo = 'output.csv'
        print(f"Saving Jobs em {nome_arquivo}...")
        
        keys = list_jobs[0].keys()
        jobs_existentes = set()

        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r', newline='', encoding='utf-8') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    if 'jobtitle' in row:
                        jobs_existentes.add(row['jobtitle'])

        novos_jobs = [job for job in list_jobs if job.get('jobtitle') not in jobs_existentes]

        if novos_jobs:
            arquivo_novo = not os.path.exists(nome_arquivo)
            
            with open(nome_arquivo, 'a', newline='', encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys)
                
                if arquivo_novo:
                    dict_writer.writeheader()
                    
                dict_writer.writerows(novos_jobs) 
            print(f"{len(novos_jobs)} novos jobs adicionados.")
        else:
            print("Nenhum job novo para adicionar.")
                            
                        