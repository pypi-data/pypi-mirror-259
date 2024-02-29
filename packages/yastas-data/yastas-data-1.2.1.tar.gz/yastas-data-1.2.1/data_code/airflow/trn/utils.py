from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from airflow.hooks.base_hook import BaseHook
from datetime import timedelta
import datetime
import json
import gcsfs
import ast

archivo_config = '/home/airflow/gcs/data/yas-sii/conf.json'

#lee variables para el ambiente
def recupera_be_conf(archivo_conf=archivo_config):
    """
    Lee la configuracion desde un archivo de propiedades
    :return: json de configuracion
    """
    print(archivo_conf)
    with open(archivo_conf) as f:
        be_conf = json.load(f)
    
    print(be_conf)
    return be_conf

conf=recupera_be_conf(archivo_config)
bucket_des = conf["bucket_des"]
bucket_raw = conf['bucket_raw']
bucket_trn =  conf["bucket_trn"]
bucket_temp_path=f"gs://{conf['bucket_tmp']}/CTA/"
project_id=conf["proy_sii"]
gce_region=conf["region"]
gce_zone=["zone"]
machineType_exe = conf["machine_type"]
conn_account = conf["conn_account_sii"]
service_account = conf["service_account_sii"]
snetwork = conf["snetwork"]


args = {
    'owner': 'sii-dwh',
    'depends_on_past': False,
    'email': service_account,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes = 5),
    'catchup': False,
    'dataflow_default_options': {
        'project'      : project_id,
        'zone'         : gce_zone,
        'tempLocation' : bucket_temp_path,
        'machineType'  : machineType_exe,
        'subnetwork'   : snetwork,
        'serviceAccountEmail': service_account,
    }
}

def subdag_trn(dag, parent_dag_name, child_dag_name, json_gs,**kwargs):
    connection_airflow_yas_sa_sii_de = BaseHook.get_connection(conn_account)
    service_account_yas_sa_sii_de = ast.literal_eval(connection_airflow_yas_sa_sii_de.extra_dejson["keyfile_dict"])

    # Datos Generales para la ejecucion
    project         = conf["proy_sii"]
    snetwork        = conf["snetwork"]
    service_account_email = conf['service_account_sii']
    machine_type    = conf['machine_type']
    with gcsfs.GCSFileSystem(project=project, token=service_account_yas_sa_sii_de).open(json_gs) as f:
        jd = json.load(f)
    # Variables para ejecucion desde JSON
    url_raw = f"gs://{bucket_raw}/{jd['app']}/raw_{jd['table_name']}/"

    # Datos de TRN
    job_name_trn  = jd['job_name']
    url_trn       =  f"gs://{bucket_trn}/{jd['app']}/trn_{jd['table_name']}/"
    file_name_trn = f"trn_{jd['table_name']}"
    trn_template  = f"gs://{bucket_des}/{jd['app']}/TRN/tpl/{jd['trn_template_name']}" 
    
    folders = gcsfs.GCSFileSystem(project=project, token=service_account_yas_sa_sii_de).ls(url_raw)
    folders.sort()
    folder = folders[-1]
    
    date_folder = folder.split('/')[3]
    if len(date_folder)==10:
        url_source = f"gs://{folder}/raw_{jd['table_name']}-00000-of-00001.parquet"
        url_dest   = url_trn + date_folder+'/'+file_name_trn
        parent_dag_name_for_id = parent_dag_name.lower()
        
        print('url_source: ' + url_source)
        print('url_dest: ' + url_dest)
        
        dataflow = DataflowTemplatedJobStartOperator(
        task_id=f'{parent_dag_name_for_id}-{child_dag_name}',
        job_name=f'{job_name_trn}-{date_folder}',
        template=trn_template,
        location="us-east1",
        gcp_conn_id=conn_account,
                parameters={
                    'url_raw' : url_source,
                    'url_trn' : url_dest,
                    'folder_date': str(datetime.date.today()),
                },
        options={
            "subnetwork":snetwork,
            "serviceAccountEmail":service_account_email,
        },
        dataflow_default_options={
                'project'      : project,
                'zone'         : conf['zone'],
                'tempLocation' : f"gs://{conf['bucket_tmp']}/CTA/",
                'machineType'  : machine_type,
                'subnetwork'   : snetwork,  
                'serviceAccountEmail': service_account_email,
                'ipConfiguration': 'WORKER_IP_PRIVATE',
            },
            dag=dag,
        )
        dataflow.execute(context=kwargs)