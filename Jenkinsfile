pipeline {
    agent any


    environment {
        // Azure credentials
        SWA_DEPLOYMENT_TOKEN = credentials('swa_deployment_token')


        AZURE_CLIENT_ID = credentials('azure_client_id')
        AZURE_CLIENT_SECRET = credentials('azure_client_secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        AZURE_SUBSCRIPTION_ID = credentials('azure_subscription_id')


        // Database (required only because Jenkins runs Alembic)
        DB_URL = credentials('db_url')


        // Azure resources
        AZURE_RESOURCE_GROUP = 'PriyanshuChetanRG'
        SWA_APP_NAME = 'chetansFE'
        APP_SERVICE = 'PriyanshusBE'


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


                sh '''
                    git fetch --tags || true
                '''
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
                      --username $AZURE_CLIENT_ID \
                      --password $AZURE_CLIENT_SECRET \
                      --tenant $AZURE_TENANT_ID


                    az account set \
                      --subscription $AZURE_SUBSCRIPTION_ID
                '''
            }
        }


        stage('Install pnpm') {
            steps {
                sh 'npm install -g pnpm'
                sh 'pnpm --version'
                sh 'pnpm add -D sass-embedded'


            }
        }


        stage('Frontend Dependencies') {
            steps {
                dir("${STATIC_APP_PATH}") {
                    sh 'pnpm ci --ignore-scripts'
                    sh 'pnpm install --frozen-lockfile'
                    sh 'pnpm approve-builds'
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
                          --deployment-token $SWA_DEPLOYMENT_TOKEN \
                          --env production
                    '''
                }
            }
        }


        


        stage('Verify Redis Connectivity') {
            steps {
                echo 'Redis should already exist. Verify connectivity using application health checks or Azure Monitor.'
            }
        }


       stage('Run Alembic Migrations') {
    steps {
        dir("${BACKEND_PATH}") {
            sh '''
                export DB_URL="$DB_URL"

                python3 -m pip install --upgrade pip
                python3 -m pip install poetry

                poetry config virtualenvs.in-project true

                poetry install --no-interaction --no-root

                python3 -c "import os; print('DB_URL exists:', bool(os.getenv('DB_URL')))"

                poetry run alembic upgrade head
            '''
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
                    az webapp deployment source config-zip \
                      --resource-group $AZURE_RESOURCE_GROUP \
                      --name $APP_SERVICE \
                      --src backend.zip
                '''
            }
        }


        stage('Restart App Service') {
            steps {
                sh '''
                    az webapp restart \
                      --resource-group $AZURE_RESOURCE_GROUP \
                      --name $APP_SERVICE
                '''
            }
        }
    }


    post {
        success {
            echo "Version ${env.APP_VERSION} deployed successfully."
        }


        failure {
            echo "Deployment failed. Check logs above."
        }


        always {
            cleanWs()
        }
    }
}

