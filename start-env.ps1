Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
do { Start-Sleep 5; docker info *> $null } until ($LASTEXITCODE -eq 0)
minikube start --driver=docker
kubectl wait --for=condition=Ready node --all --timeout=180s
kubectl wait --for=condition=Ready pod --all -n default --timeout=300s
kubectl wait --for=condition=Ready pod --all -n monitoring --timeout=300s
Get-Process kubectl -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Process kubectl -WindowStyle Hidden -ArgumentList "port-forward -n monitoring svc/prometheus-grafana 3000:80"
Start-Process kubectl -WindowStyle Hidden -ArgumentList "port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090:9090"
"Ready: http://localhost:3000 and http://localhost:9090"
