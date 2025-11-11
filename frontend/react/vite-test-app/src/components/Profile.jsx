import kevinPhoto from '../assets/kevin_willi_table_left.PNG';
import '../app.css'; 

const Profile = ({ Name = "Taif", Email = "Test@mail.com", Phone = 1234567890 }) => {
  return (
    <table className="profile-table">
      <tbody>
        <tr>
          <td rowSpan="3" className="profile-photo-cell">
            <img src={kevinPhoto} alt="Profile" className="profile-photo" />
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
  );
};

export default Profile;


// export Txt = ()=> {return "hi"}
export const Txt = ()=>{
  const use_variable = 'string in variable within {}'
  const use_function = () => 'calling function in {}'
  return (
    <>
    Variable: {use_variable}<br/>
    Function: {use_function()}<br/>
    Arth: {"2" - 2}<br/>
    Ternry: {2>1?'true':'false'}<br/>
    Map : {["seven","three","eight"].map((string)=>{
      return string + " "
    })}
    <p>test p tag for multiple named export</p>
    </>
  )
}
