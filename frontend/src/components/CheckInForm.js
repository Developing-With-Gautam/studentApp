import React, { useState } from "react";
import { API_URL } from "../api";

function CheckInForm({ onCheckIn }) {
  const [studentId, setStudentId] = useState("");
  const [loading, setLoading] = useState(false);

  const handleCheckIn = async () => {
    if (!studentId) return alert("Enter student ID");
    setLoading(true);
    try {
      const res = await fetch(`${API_URL}/check_in`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ student_id: studentId }),
      });

      if (!res.ok) throw new Error("Check-in failed");

      const data = await res.json();
      onCheckIn(data);
      setStudentId("");
    } catch (err) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Student ID"
        value={studentId}
        onChange={(e) => setStudentId(e.target.value)}
      />
      <button onClick={handleCheckIn} disabled={loading}>
        {loading ? "Checking..." : "Check In"}
      </button>
    </div>
  );
}

export default CheckInForm;
