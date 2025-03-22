-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 22, 2025 at 09:21 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rlwy_consession`
--

-- --------------------------------------------------------

--
-- Table structure for table `concession_forms`
--

CREATE TABLE `concession_forms` (
  `Fee_Rec_No` int(5) NOT NULL,
  `Fees_Payment_Date` date NOT NULL,
  `Mobile_No` int(10) NOT NULL,
  `Student_ID` varchar(10) NOT NULL,
  `Dept_Rlwy_Name` varchar(15) NOT NULL,
  `Dept_Station` varchar(50) NOT NULL,
  `Arrival_Rlwy_Name` varchar(15) NOT NULL,
  `Arrival_Station` varchar(8) NOT NULL,
  `Pass_Duration` varchar(9) NOT NULL,
  `Tkt_Class` varchar(11) NOT NULL,
  `Pre_Tkt_Expire_Date` date NOT NULL,
  `Pre_Cert_No` int(10) NOT NULL,
  `Status` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `concession_forms`
--

INSERT INTO `concession_forms` (`Fee_Rec_No`, `Fees_Payment_Date`, `Mobile_No`, `Student_ID`, `Dept_Rlwy_Name`, `Dept_Station`, `Arrival_Rlwy_Name`, `Arrival_Station`, `Pass_Duration`, `Tkt_Class`, `Pre_Tkt_Expire_Date`, `Pre_Cert_No`, `Status`) VALUES
(1, '0000-00-00', 2147483647, '2023B1080', 'Western Rly', 'Mumbai Central', 'Western Rly', 'Malad', 'Quarterly', '2nd', '0000-00-00', 84562564, 'Rejected'),
(2, '2025-02-02', 2147483647, '2023B1081', 'Western Rly', 'Mumbai Central', 'Western Rly', 'Malad', 'Quarterly', '2nd', '2025-02-02', 84562565, 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `registered_students`
--

CREATE TABLE `registered_students` (
  `Student_ID` varchar(10) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `DOB` date NOT NULL,
  `Year` int(4) NOT NULL,
  `C_Address` varchar(255) NOT NULL,
  `P_Address` varchar(255) NOT NULL,
  `Branch` varchar(5) NOT NULL,
  `Class` varchar(5) NOT NULL,
  `Roll_ID` varchar(5) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registered_students`
--

INSERT INTO `registered_students` (`Student_ID`, `Gender`, `Name`, `DOB`, `Year`, `C_Address`, `P_Address`, `Branch`, `Class`, `Roll_ID`, `Email`, `Password`) VALUES
('202302B107', 'Male', 'Prathamesh Sitaram Warak', '0000-00-00', 2023, 'Mumbai', 'Mumbai', 'INFT', 'SEIT2', '79', 'Prathameshwarak-inft@atharvacoe.ac.in', 'Prathamesh@123'),
('20232B1080', 'Male', 'Mihir D. Chavan', '0000-00-00', 2023, 'Mumbai', 'Mumbai', 'INFT', 'SEIT2', '80', 'mihirchavan-inft@atharvacoe.ac.in', 'Mihir@123');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Role` varchar(10) NOT NULL,
  `TimeStamp` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Email`, `Password`, `Role`, `TimeStamp`) VALUES
('Admin@admin.com', 'Admin@123', 'Admin', '0000-00-00 00:00:00.000000'),
('Prathameshwarak-inft@atharvacoe.ac.in', 'Prathamesh@123', 'student', '0000-00-00 00:00:00.000000'),
('mihirchavan-inft@atharvacoe.ac.in', 'Mihir@123', 'student', '2025-03-22 07:05:03.769566');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registered_students`
--
ALTER TABLE `registered_students`
  ADD PRIMARY KEY (`Student_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
