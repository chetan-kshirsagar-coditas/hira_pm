pipeline {
    agent any

    environment {
        // Here we need the Azure Static Web Apps deployment token - overview page top right corner
        SWA_DEPLOYMENT_TOKEN = credentials('swa_deployment_token')

        // Service Principal credentials
        AZURE_CLIENT_ID       = credentials('azure_client_id')
        AZURE_CLIENT_SECRET   = credentials('azure_client_secret')
        AZURE_TENANT_ID       = credentials('azure-tenant-id')
        AZURE_SUBSCRIPTION_ID = credentials('azure_subscription_id')

        //  Static Web App details
        SWA_APP_NAME          =  'chetansFE'
        AZURE_RESOURCE_GROUP  =  'PriyanshuChetanRG'
    }

    tools {
        nodejs 'NodeJS-20'  // Remember to match name in Jenkins > Manage Jenkins > Tools veryyyyyyyyyy imp
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install pnpm') {
            steps {
                sh 'npm install -g pnpm'
                sh 'pnpm --version'
                sh 'pnpm add -D sass-embedded'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('frontend') {
                    sh 'pnpm ci --ignore-scripts'
                    sh 'pnpm install --frozen-lockfile'
                    sh 'pnpm approve-builds'
                }
            }
        }

       // stage('Lint') {
           // steps {
              //  dir('frontend') {
                   // sh 'pnpm lint'
                //}
            //}
      //  }

        stage('Build') {
            steps {
                dir('frontend') {
                    sh 'pnpm build'
                }
            }
        }

        stage('Install SWA CLI') {
            steps {
                sh 'npm install -g @azure/static-web-apps-cli'
                sh 'swa --version'
            }
        }

        stage('Azure Login (Service Principal)') {
            steps {
                sh '''
                    az login \
                        --service-principal \
                        --username $AZURE_CLIENT_ID \
                        --password $AZURE_CLIENT_SECRET \
                        --tenant $AZURE_TENANT_ID

                    az account set --subscription $AZURE_SUBSCRIPTION_ID
                '''
            }
        }

        stage('Deploy to Azure Static Web Apps') {
            steps {
                dir('frontend') {
                    sh '''
                        swa deploy ./dist \
                            --deployment-token $SWA_DEPLOYMENT_TOKEN \
                            --env production
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Frontend deployed successfully to Azure Static Web Apps!"
        }
        failure {
            echo " Deployment failed. Check logs above."
        }
        always {
            cleanWs()
        }
    }
}
