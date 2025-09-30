import React from "react";

function CheckInTable({ checkins }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Student Name</th>
          <th>Time</th>
        </tr>
      </thead>
      <tbody>
        {checkins.map((c, index) => (
          <tr key={index}>
            <td>{c.student_name || c.student_id}</td>
            <td>{new Date(c.timestamp).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default CheckInTable;
