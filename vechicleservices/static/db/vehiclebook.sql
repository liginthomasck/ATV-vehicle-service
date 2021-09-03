-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 03, 2020 at 09:54 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `vehiclebook`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE IF NOT EXISTS `bookings` (
  `bid` int(10) NOT NULL AUTO_INCREMENT,
  `vid` int(10) NOT NULL,
  `vname` varchar(20) NOT NULL,
  `color` varchar(20) NOT NULL,
  `qty` varchar(10) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`bid`, `vid`, `vname`, `color`, `qty`, `status`) VALUES
(1, 4, 'Honda amaze', 'white', '1', 'book'),
(2, 1, 'Honda amaze', 'white', '1', 'book'),
(3, 5, 'Honda amaze', 'white', '1', 'book'),
(4, 6, 'Honda amaze', 'white', '1', 'book');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `uid` int(10) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `utype` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uid`, `pass`, `utype`, `email`) VALUES
(0, 'admin', 'admin', 'admin'),
(1, 'advait', 'user', 'advait@gmail.com'),
(2, 'anil', 'user', 'anilm@gmail.com'),
(3, 'alan', 'user', 'alanss@gmail.com'),
(4, 'aryan', 'user', 'aryan@gmail.com'),
(5, 'neethus', 'user', 'neethus@gmail.com'),
(6, 'krishna', 'user', 'krishna@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `mechanics`
--

CREATE TABLE IF NOT EXISTS `mechanics` (
  `mid` int(10) NOT NULL AUTO_INCREMENT,
  `mname` varchar(20) NOT NULL,
  `phno` varchar(12) NOT NULL,
  `email` varchar(20) NOT NULL,
  `addr` varchar(50) NOT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `mechanics`
--

INSERT INTO `mechanics` (`mid`, `mname`, `phno`, `email`, `addr`) VALUES
(1, 'Arun', '8900000000', 'arun@gmail.com', 'Arun Bhavan,adoor');

-- --------------------------------------------------------

--
-- Table structure for table `pay`
--

CREATE TABLE IF NOT EXISTS `pay` (
  `pid` int(10) NOT NULL AUTO_INCREMENT,
  `vid` int(10) NOT NULL,
  `advamt` varchar(10) NOT NULL,
  `bank` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `pay`
--

INSERT INTO `pay` (`pid`, `vid`, `advamt`, `bank`, `status`) VALUES
(1, 4, '50000', '', 'paid'),
(2, 4, '250', '', 'paid'),
(3, 1, '50000', '', 'paid'),
(4, 5, '50000', '', 'paid'),
(5, 6, '50000', '', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `service`
--

CREATE TABLE IF NOT EXISTS `service` (
  `sid` int(10) NOT NULL AUTO_INCREMENT,
  `vid` int(10) NOT NULL,
  `cat` varchar(20) NOT NULL,
  `vname` varchar(20) NOT NULL,
  `vmodel` varchar(20) NOT NULL,
  `vbrand` varchar(20) NOT NULL,
  `vno` varchar(12) NOT NULL,
  `sdate` varchar(10) NOT NULL,
  `stime` varchar(10) NOT NULL,
  `dtype` varchar(20) NOT NULL,
  `stype` varchar(20) NOT NULL,
  `stype2` varchar(20) NOT NULL,
  `sdate2` varchar(10) NOT NULL,
  `stype3` varchar(20) NOT NULL,
  `sdate3` varchar(10) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `service`
--

INSERT INTO `service` (`sid`, `vid`, `cat`, `vname`, `vmodel`, `vbrand`, `vno`, `sdate`, `stime`, `dtype`, `stype`, `stype2`, `sdate2`, `stype3`, `sdate3`, `status`) VALUES
(1, 4, 'four wheeler', 'Amaze', 'vxl', 'Maruti', 'kl261234', '2020-02-13', '01:00', 'Self', 'water service', '', '', '', '', 'Approve'),
(2, 5, 'Four wheeler', 'Amaze', 'VLX', 'Honda', 'kl234566', '2020-06-03', '12:00', 'self', 'water service', '', '', '', '', 'Approve'),
(3, 6, 'four wheeler', 'Wagonor', 'lxi', 'Maruti', 'kl263445', '2020-06-03', '02:10', 'self', 'water service', '', '', '', '', 'Approve');

-- --------------------------------------------------------

--
-- Table structure for table `servicedone`
--

CREATE TABLE IF NOT EXISTS `servicedone` (
  `sdid` int(10) NOT NULL AUTO_INCREMENT,
  `vid` int(10) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `vtype` varchar(20) NOT NULL,
  `vno` varchar(10) NOT NULL,
  `sd` varchar(50) NOT NULL,
  `amt` varchar(10) NOT NULL,
  `sstatus` varchar(20) NOT NULL,
  `stype` varchar(20) NOT NULL,
  PRIMARY KEY (`sdid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `servicedone`
--

INSERT INTO `servicedone` (`sdid`, `vid`, `fname`, `vtype`, `vno`, `sd`, `amt`, `sstatus`, `stype`) VALUES
(1, 4, 'Aryan', 'vxl', 'kl261234', 'water service', '250', 'Completed', 'free service'),
(2, 5, 'neethu shaji', 'VLX', 'kl234566', 'water service', '250', 'Completed', 'Paid service'),
(3, 6, 'krishna', 'lxi', 'kl263445', 'water service', '300', 'Completed', 'paid service'),
(4, 6, 'krishna', 'lxi', 'kl263445', 'water service', '250', 'Completed', 'Paid service');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `ph` varchar(12) NOT NULL,
  `email` varchar(20) NOT NULL,
  `rdate` varchar(10) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `name`, `ph`, `email`, `rdate`) VALUES
(1, 'Advait', '9087654436', 'advait@gmail.com', '2020-02-11'),
(2, 'Anil kumar m', '9089098767', 'anilm@gmail.com', '2020-02-11'),
(3, 'alan', '9087098098', 'alanss@gmail.com', '2020-02-11'),
(4, 'Aryan', '8978909890', 'aryan@gmail.com', '2020-02-12'),
(5, 'neethu shaji', '9880767697', 'neethus@gmail.com', '2020-06-03'),
(6, 'krishna', '7869868969', 'krishna@gmail.com', '2020-06-03');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE IF NOT EXISTS `vehicle` (
  `vehid` int(10) NOT NULL AUTO_INCREMENT,
  `mno` varchar(10) NOT NULL,
  `mname` varchar(20) NOT NULL,
  `color` varchar(20) NOT NULL,
  `scap` varchar(10) NOT NULL,
  `fea` varchar(50) NOT NULL,
  `mil` varchar(10) NOT NULL,
  `amt` varchar(10) NOT NULL,
  `img` varchar(50) NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`vehid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`vehid`, `mno`, `mname`, `color`, `scap`, `fea`, `mil`, `amt`, `img`, `status`) VALUES
(1, 'vxl', 'Honda amaze', 'white', '5', 'Full Option', '125', '5000000', 'amaze.jfif', 'available');
