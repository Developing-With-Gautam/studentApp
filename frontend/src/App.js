import React, { useEffect, useState } from "react";
import StudentForm from "./components/StudentForm";
import StudentTable from "./components/StudentTable";
import CheckInForm from "./components/CheckInForm";
import CheckInTable from "./components/CheckInTable";
import { API_URL } from "./api";
import "./App.css";

function App() {
  const [students, setStudents] = useState([]);
  const [checkins, setCheckins] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Fetch students
  const fetchStudents = async () => {
    try {
      console.log("Fetching students from:", `${API_URL}/students`);
      const res = await fetch(`${API_URL}/students`);
      if (!res.ok) throw new Error("Failed to fetch students");
      const data = await res.json();
      setStudents(data);
    } catch (err) {
      console.error(err);
      setError(err.message);
    }
  };

  // Fetch check-ins
  const fetchCheckIns = async () => {
    try {
      console.log("Fetching check-ins from:", `${API_URL}/check_in`);
      const res = await fetch(`${API_URL}/check_in`);
      if (!res.ok) throw new Error("Failed to fetch check-ins");
      const data = await res.json();
      setCheckins(data);
    } catch (err) {
      console.error(err);
      setError(err.message);
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      await fetchStudents();
      await fetchCheckIns();
      setLoading(false);
    };
    fetchData();
  }, []);

  const addStudent = (student) => setStudents([...students, student]);
  const addCheckIn = (checkin) => setCheckins([...checkins, checkin]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p style={{ color: "red" }}>Error: {error}</p>;

  return (
    <div className="container">
      <h1>Student Dashboard</h1>

      <div className="section">
        <h2>Add Student</h2>
        <StudentForm onAdd={addStudent} />
        <h3>All Students</h3>
        <StudentTable students={students} />
      </div>

      <div className="section">
        <h2>Check In</h2>
        <CheckInForm onCheckIn={addCheckIn} />
        <h3>All Check-ins</h3>
        <CheckInTable checkins={checkins} />
      </div>
    </div>
  );
}

export default App;
