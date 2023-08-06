# k8-excelFile-to-yaml

In day to day work, Applictaion team develop the application and hand it over to Deployment team. Or Sometimes App team engage their BAs for deployment to be happend.
Deployment team expect correct data from Application team so if there will any issue then App team will be responsible.
Excel sheet is the best way to connect Application team and DevOps team for sharing data.
**1. App team share the data with DevOps team.
2. DevOps team validate all the required data and naming convention.
3. Using the small lines of code Devops team can fetch the details from execl sheet and create Yaml file out of it.
4. During the change windows DevOps team can use the same file for deployment.**

Here we have 
**DeploymentDetails.xlsx** --> all the deploayment details has been mention here.
**GenerateDeploy.py** --> It will fetch the data from execl sheet and create yaml file.
**Deploymnet.yaml** --> generated yaml file
