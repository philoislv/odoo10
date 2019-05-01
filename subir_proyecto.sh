#bin/bash
#Nos identificamos
git config --global user.email "aolmolopez97@gmail.com"
git config --global user.name "Antonio"
#Añadimos lo que queremos subir
git add .
#Hacemos commit
git commit -m "Subida de Proyecto"
#Hacemos push y lo subimos arriba
git push -u origin master
echo "Subido"
