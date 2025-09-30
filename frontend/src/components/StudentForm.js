import React, { useState } from "react";
import { API_URL } from "../api";

function StudentForm({ onAdd }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [studentId, setStudentId] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(`${API_URL}/students`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, student_id: studentId }),
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Failed to add student");

      onAdd(data);
      setName("");
      setEmail("");
      setStudentId("");
    } catch (err) {
      alert("Error adding student: " + err.message);
      console.error("Add student error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Student ID"
        value={studentId}
        onChange={(e) => setStudentId(e.target.value)}
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? "Adding..." : "Add Student"}
      </button>
    </form>
  );
}

export default StudentForm;
