
# File-Simetrik-Prueba

* Aspectos a tener en cuenta para la instalación y ejecución del proyecto.
     
     1) Instalar las dependencias que se encuentran en el archivo requirements.txt con el comando pip install -r requirements.txt 
     2) Pararse sobre la carpeta filesSimetrik y ejecutar el comando python manage.py runserver, para así ejecutar el proyecto.
     3) Dentro de la carpeta filesSimetrik/filesSimetrik, se encuentra un archivo .env el cual contiene la variables de entorno como las credenciales de la base de datos, las key e id de S3,
        el nombre del archivo csv, del bucket, el nombre de la tabla de la base de datos.
         
     
* Vistas a consultar via postman o Talend API Tester

    1) En alguna de estas aplicaciones colocar la url del servidor/getFile y metodo GET. Cuando se orpima el botón SEND se extraera el archivo de S3 y se crceara la tabla en una base de datos externa
       En el body response de la aplicación se debe ver una respuesta de 200 y un mensaje que diga "Archivo obtenido y cargado a base de datos correctamente". A esta vista solo se podra acceder una vez
        Puesto que al crear la tabla cuando se ejecute de nuevo un error saltara advirtiendo que la tabla ya existe.
        
    2) Colocar la url del servidor/filter y metodo GET. En esta vista se debe especificar la propiedad mediante la cual se desea hacer el filtrado. El archivo que se descargará de AWS contara con
      las siguiente columnas, index, id, first_name, last_name, email, gender e ip_address, se debe escribir en la url el nombre de la o las columnas a filtrar, por ejemplo, url del servidor/filter?first_name=Jeremie.
      Cuando se de SEND el body response traera en formato JSON los objetos que tengan por nombre Jeremie, así mismo cuando se filtre una cantidad considerable de elementos se podrá especificar la pagina que se desea 
      mostrar en el body response, un ejemplo seria url del servidor/filter?gender=Male, una gran cantidad de objetos se renderizaran en la pagina, por lo que limite la cantidad de objetos a 5 por pagina, se debera especificar
      en la url la pagina a consultar de la siguiente manera. servidor/filter?gender=Male&page=2, esta url mostrara los siguientes 5 objetos filtrados de la base de datos y asi con cualquier columna que sse desee consultar.
      Tambien se puede hacer filtrados especificos combinando mas de una columna a filtrar, servidor/filter?firs_name=Jeremie&last_name=Ber&gender=male.
      
     3) Colocar la url del servidor/reorder y metodo GET. Esta vista re ordenara las columnas del dataframe, mas no de la base de datos, de la siguiente manera 'gender','first_name','id','email','ip_address','last_name','index'
        y al igual que en el filtrado se puede especificar la pagina a la que se quiere ir puesto que son muchos datos, url del servidor/reorder?page=4, si no se especifica pagina simplemente muestra la pagina 1.
       
* Test Unitarios
      
      Para estos test utilicé el archivo tests que django crea por defecto cuando se crea la aplicación. Dentro de este archivo generé tres tests de cada una de las vistas descritas previamente,
      basicamente solo evalue que se devolviera un status_code de 200. 
      Para ejecutar los tests pararse sobre la carpeta del proyecto y ejectutar el comando python manage.py test.
      
* Tecnologias que usé

    1) AWS S3 para almacenar el archivo csv
    2) pandas para extraer el archivo
    3) SQLAlchemy para mapear la tabla de dataframe a SQL
    4) Postgres como motor de bases de datos
    5) django como framework para API Rest
    6) Talend API Tester como herramienta para ver el comportamiento de mis URL, equivalete a POSTMAN.

       
