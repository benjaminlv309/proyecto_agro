-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-11-2026 a las 22:10:29
-- Versión del servidor: 10.11.16-MariaDB
-- Versión de PHP: 8.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agro_bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agroapp_registroactividad`
--

CREATE TABLE `agroapp_registroactividad` (
  `id` bigint(20) NOT NULL,
  `responsable` varchar(100) NOT NULL,
  `actividad` longtext NOT NULL,
  `parcela` varchar(50) NOT NULL,
  `fecha_registro` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `agroapp_registroactividad`
--

INSERT INTO `agroapp_registroactividad` (`id`, `responsable`, `actividad`, `parcela`, `fecha_registro`) VALUES
(1, 'Juan Pérez', 'Se realizó el riego de los cultivos.', 'Parcela 03', '2026-11-16 19:01:35.994120'),
(2, 'Esteban Paredes', 'Riego de parcela', 'Parcela 05', '2026-11-16 20:33:03.307013');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agroapp_registroactividad`
--
ALTER TABLE `agroapp_registroactividad`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agroapp_registroactividad`
--
ALTER TABLE `agroapp_registroactividad`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
