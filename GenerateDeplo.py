import pandas as pd

dict_Data = {}
excel_Loc = 'D:\\PythonProjects\\Python\\DeploymentDetails.xlsx'
yaml_file = 'D:\\PythonProjects\\Python\\Deployment.yaml'

def readExcel(excel_Loc):
    dataDeploy = pd.read_excel(excel_Loc,sheet_name='Deployment')
    #excel_header = data.columns.tolist()
    return dataDeploy

def load_data(data):
    for _, row in data.iterrows():
        dict_Data['deploy_name'] = row['deploy_name']
        dict_Data['deploy_labels'] = row['deploy_labels']
        dict_Data['ns_name'] = row['namespace']
        dict_Data['replicas'] = row['replicas']
        dict_Data['selector'] = row['selector']
        dict_Data['pod_labels'] = row['pod_labels']
        dict_Data['containers_name'] = row['containers_name']
        dict_Data['containers_image'] = row['containers_image']
        dict_Data['containers_port'] = row['containers_port']
    return dict_Data
def generate_yaml(Deploy_data,yaml_file):
    deploy_data = f"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {Deploy_data['deploy_name']}
  namespace: {Deploy_data['ns_name']}
  labels:
    {Deploy_data['deploy_labels']}
spec:
  replicas: {Deploy_data['replicas']}
  selector:
    matchLabels:
      {Deploy_data['selector']}
  template:
    metadata:
      labels:
        {Deploy_data['pod_labels']}
    spec:
      containers:
      - name: {Deploy_data['containers_name']}
        image: {Deploy_data['containers_image']}
        ports:
        - containerPort: {Deploy_data['containers_port']}
                    """
    write_yaml = open(yaml_file,'w')
    write_yaml.writelines(deploy_data)
    print(deploy_data)




if __name__ == "__main__":
  data = readExcel(excel_Loc)
  Deploy_data = load_data(data)
  generate_deployfile = generate_yaml(Deploy_data,yaml_file)
