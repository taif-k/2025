import kevinPhoto from '../assets/images/kevin_willi_table_left.PNG';

const Profile = (props) => {
const { Name = "test name", Email = "testemail@mail.com", Phone = 1234567890, imgg = kevinPhoto  } = props
  return (
    <>
      <table className="profile-table">
        <tbody>
          <tr>
            <td rowSpan="3" className="profile-photo-cell">
              <img src={imgg} alt="Profile" className="profile-photo" />
            </td>
            <td className="profile-label">Name</td>
            <td>{Name}</td>
          </tr>
          <tr>
            <td className="profile-label">Email</td>
            <td>{Email}</td>
          </tr>
          <tr>
            <td className="profile-label">Phone</td>
            <td>{Phone}</td>
          </tr>
        </tbody>
      </table>
      {!Name && <Avatar imgg={imgg} />}
    </>

  );
};

export default Profile;


export const Avatar = ({imgg}) => {
  return (
    <>
      <img src={imgg} alt="Avatar" />
    </>
  )
}
