# Crear base de datos
create database mensajero;

# Dar privilegios al usuario dentro de la base de datos
grant all on mensajero.* to 'local_user' @'localhost';

# Crear tabla de usuarios
create table mensajero.user (
    id int not null auto_increment, username varchar(50) not null, nombre varchar(50) not null, apellido varchar(50) not null, email varchar(100) not null, primary key (id)
);

# Insertar usuario admin de la aplicacion
insert into
    mensajero.user (
        username, nombre, apellido, email
    )
values (
        'admin', 'User', 'Admin', 'admin@mail.com'
    );

# Crear tabla de comentarios
create table mensajero.notas (
    id int not null auto_increment, creator int not null, texto varchar(250), primary key (id), foreign key (creator) references user (id)
);