# My Django Project

This is a Django project template.

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)
![Python](https://img.shields.io/badge/Python-3.10.x-lightblue)
![Django](https://img.shields.io/badge/Django-4.2.x-blue)
![Boostrap](https://img.shields.io/badge/Boostrap-5.x-yellow)
![HTML](https://img.shields.io/badge/HTML-5-violet)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.x-orange)
![Docker](https://img.shields.io/badge/Docker-20.x-blue)

## Pasos

1. Crear 3 Archivos requirements.txt Dockerfile docker-compose.yml

2. Configurar los archivos Estos archivos son los que están en el ejemplo con la configuración predeterminada

3. Ejecutar el comando:

```sh
docker build -t django_app .
```
(Va con el punto al final)

```sh
docker-compose up
```

4. Ingresamos al VSC al Docker con el Explorador remoto y creamos las carpetas extras

```sh
mkdir -p ./{templates,media,static/{css,js,img,lib}}
```

5. Ejecutar celery y rabbit
```sh
celery -A plants_gift worker -l info
```
```sh
celery -A plants_gift flower
```

## License

This project is licensed under the MIT License.

## Contacto

- **Correo Electrónico**: alucase@gmail.com
- **LinkedIn**: [Lucas Acosta](https://www.linkedin.com/in/alucase/)
- **GitHub**: [ALucasE](https://github.com/ALucasE)
- **Web**: [alucase.github.io](https://alucase.github.io/)

---

¡Gracias por visitar mi github! Espero que disfrutes explorando mis proyectos.
