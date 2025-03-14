from shareplum import Site,Office365
from shareplum.site import Version
from boto3.session import Session
from datetime import datetime

todayDate = datetime.today().strftime('%Y-%m-%d')

ACCESS_KEY = ${{secrets.AWS_ACCESS_KEY}}
SECRET_KEY = ${{secrets.AWS_ACCESS_SECRET}}

session = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY)

bucket_name = 'esx-dteng-bkt'
bucket = session.resource('s3').Bucket(bucket_name)
filepath = 'chartofaccounts/ChartOfAccounts_2025-03-14T16:32:22.964694424Z.json'
authcookie = Office365('https://parroquialalaguna0.sharepoint.com/', username='data@parroquialalaguna.com',password='fS939507082305*').GetCookies()
site = Site('https://parroquialalaguna0.sharepoint.com/sites/DatosLaLaguna/',version=Version.v365,authcookie=authcookie); 
file_name='ChartOfAccounts_'+todayDate+'.json'

for obj in bucket.objects.all():
    if obj.key==filepath:
        body = obj.get()['Body'].read()

outputFolder = site.Folder('Documentos%20compartidos/EssexTesting')

outputFolder.upload_file(body,file_name)
