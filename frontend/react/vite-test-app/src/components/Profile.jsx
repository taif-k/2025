import React from 'react'
import kevinPhoto from '../assets/kevin_willi_table_left.PNG';


const Profile = (props) => {
  const { Name = "Taif", Email = "Test@mail.com", Phone = 1234567890 } = props
  return (
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <tbody>
        <tr>
          <td
            rowSpan="2"
            style={{
              width: "150px",
              textAlign: "center",
              verticalAlign: "middle",
              borderRight: "1px solid #ddd",
            }}
          >
            <img
              src={kevinPhoto}
              alt="Profile"
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
              }}
            />
          </td>

          <td style={{ fontWeight: "bold", padding: "8px", width: "30%" }}>
            Name
          </td>
          <td style={{ padding: "8px" }}>{Name}</td>
        </tr>

        <tr>
          <td style={{ fontWeight: "bold", padding: "8px" }}>Email <br /> Phone</td>
          <td style={{ padding: "8px" }}>
            {Email}<br />
            {Phone}
          </td>
        </tr>
      </tbody>
    </table>


  )
}

export default Profile
