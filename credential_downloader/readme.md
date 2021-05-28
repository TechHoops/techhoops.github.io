1. Create a virtual environment
    python -m venv .venv (You only need to do this if .venv folder does not exist in your local)
2. Everytime you need to run , activate the virtual environment    
    source .venv/Scripts/activate
3. Only once, install selenium 
    pip install selenium
4. Download chromedriver and copy in the same folder as downloadCredentials.py (ensure major version of your chrome browser matches with the driver you download) 
 https://chromedriver.chromium.org/downloads

---- run this , sit back and enjoy (Automation will push the DUO for you)---
python downloadCredentials.py

After the run a file will be created for you in you home folder .aws/credentials

to run any aws cli command add "--profile <account_type>-<env>"
e.g
clng-dev
clut-prd

## In addition create .bashrc file in your home directory for quick commands --
PATH=$PATH:/c/Program\ Files/Python38:/c/Users/cn240415/repos/bin
alias k="kubectl"
alias kcc="kubectl config current-context"
alias kgp="kubectl get pods -n "
alias kclopd='aws --profile clop-dev eks --region us-east-1 update-kubeconfig --name cnc-clop-core-dev-us-east-1'
alias kclopt='aws --profile clop-tst eks --region us-east-1 update-kubeconfig --name cnc-clop-core-tst-us-east-1'
alias kclops='aws --profile clop-stg eks --region us-east-1 update-kubeconfig --name cnc-clop-core-stg-us-east-1'
alias kclopp='aws --profile clop-prd eks --region us-east-1 update-kubeconfig --name cnc-clop-core-prd-us-east-1'
alias kclutd='aws --profile clut-dev eks --region us-east-1 update-kubeconfig --name cnc-clut-core-dev-us-east-1'
alias kclutt='aws --profile clut-tst eks --region us-east-1 update-kubeconfig --name cnc-clut-core-tst-us-east-1'
alias kcluts='aws --profile clut-stg eks --region us-east-1 update-kubeconfig --name cnc-clut-core-stg-us-east-1'
alias kclutp='aws --profile clut-prd eks --region us-east-1 update-kubeconfig --name cnc-clut-core-prd-us-east-1'
alias kclngd='aws --profile clng-dev eks --region us-east-1 update-kubeconfig --name cnc-clng-dev-us-east-1'
alias kclngt='aws --profile clng-tst eks --region us-east-1 update-kubeconfig --name cnc-clng-core-tst-us-east-1'
alias kclngs='aws --profile clng-stg eks --region us-east-1 update-kubeconfig --name cnc-clng-core-stg-us-east-1'
alias kclngp='aws --profile clng-prd eks --region us-east-1 update-kubeconfig --name cnc-clng-core-prd-us-east-1'
alias kclmdd='aws --profile clmd-dev eks --region us-east-1 update-kubeconfig --name cnc-clmd-core-dev-us-east-1'
alias kclmdt='aws --profile clmd-tst eks --region us-east-1 update-kubeconfig --name cnc-clmd-core-tst-us-east-1'
alias kclmds='aws --profile clmd-stg eks --region us-east-1 update-kubeconfig --name cnc-clmd-core-stg-us-east-1'
alias kclmdp='aws --profile clmd-prd eks --region us-east-1 update-kubeconfig --name cnc-clmd-core-prd-us-east-1'