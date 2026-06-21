pipeline {
agent any

environment {
SWA_DEPLOYMENT_TOKEN = credentials('swa_deployment_token')

AZURE_CLIENT_ID = credentials('azure_client_id')
AZURE_CLIENT_SECRET = credentials('azure_client_secret')
AZURE_TENANT_ID = credentials('azure-tenant-id')
AZURE_SUBSCRIPTION_ID = credentials('azure_subscription_id')

DB_URL = credentials('db_url')

AZURE_RESOURCE_GROUP = 'taskflow-project-rg'

SWA_APP_NAME = 'taskflow-frontend'
APP_SERVICE = 'taskflow-api'

STATIC_APP_PATH = 'frontend'
BACKEND_PATH = 'backend'

VERSION_FILE = '.version'
}

tools {
nodejs 'NodeJS-20'
}

stages {

stage('Checkout') {
steps {
checkout scm

sh 'git fetch --tags || true'
}
}

stage('Calculate Version') {
steps {
script {

def commitMsg = sh(
script: "git log -1 --pretty=%B",
returnStdout: true
).trim()

def currentVersion = fileExists(VERSION_FILE)
? readFile(VERSION_FILE).trim()
: "1.2.0"

def parts = currentVersion.tokenize('.')

int major = parts[0].toInteger()
int minor = parts[1].toInteger()
int patch = parts[2].toInteger()

if (commitMsg.contains("BREAKING CHANGE")) {
major++
minor = 0
patch = 0
} else if (commitMsg.startsWith("feat:")) {
minor++
patch = 0
} else {
patch++
}

env.APP_VERSION = "${major}.${minor}.${patch}"

writeFile file: VERSION_FILE, text: env.APP_VERSION

echo "Application version: ${env.APP_VERSION}"
}
}
}

stage('Azure Login') {
steps {
sh '''
az login \
--service-principal \
--username "$AZURE_CLIENT_ID" \
--password "$AZURE_CLIENT_SECRET" \
--tenant "$AZURE_TENANT_ID"

az account set \
--subscription "$AZURE_SUBSCRIPTION_ID"
'''
}
}

stage('Install pnpm') {
steps {
sh '''
npm install -g pnpm
pnpm --version
'''
}
}

stage('Install Frontend Dependencies') {
steps {
dir("${STATIC_APP_PATH}") {
sh 'pnpm install --frozen-lockfile'
}
}
}

stage('Build Frontend') {
steps {
dir("${STATIC_APP_PATH}") {
sh 'pnpm build'
}
}
}

stage('Install SWA CLI') {
steps {
sh '''
npm install -g @azure/static-web-apps-cli
swa --version
'''
}
}

stage('Deploy Frontend') {
steps {
dir("${STATIC_APP_PATH}") {
sh '''
swa deploy ./dist \
--deployment-token "$SWA_DEPLOYMENT_TOKEN" \
--env production
'''
}
}
}

stage('Install Backend Dependencies') {
steps {
dir("${BACKEND_PATH}") {
sh '''
python3 -m venv .venv

. .venv/bin/activate

pip install --upgrade pip

pip install poetry

poetry install --no-interaction --no-root
'''
}
}
}

stage('Run Alembic Migrations') {
steps {
dir("${BACKEND_PATH}") {
withEnv(["DB_URL=${DB_URL}"]) {

sh '''
. .venv/bin/activate

poetry run alembic upgrade head
'''
}
}
}
}

stage('Package Backend') {
steps {
dir("${BACKEND_PATH}") {
sh '''
zip -r ../backend.zip . \
-x "*.git*" \
-x "__pycache__/*" \
-x "*.pyc" \
-x ".venv/*"
'''
}
}
}

stage('Deploy Backend') {
steps {
sh '''
az webapp deploy \
--resource-group "$AZURE_RESOURCE_GROUP" \
--name "$APP_SERVICE" \
--src-path backend.zip \
--type zip
'''
}
}

stage('Restart App Service') {
steps {
sh '''
az webapp restart \
--resource-group "$AZURE_RESOURCE_GROUP" \
--name "$APP_SERVICE"
'''
}
}

stage('Health Check') {
steps {
sh '''
sleep 30

curl --fail \
https://${APP_SERVICE}.azurewebsites.net/health
'''
}
}
}

post {

success {
echo "Deployment completed successfully."
}

failure {
echo "Deployment failed."
}

always {
cleanWs()
}
}

}
       
