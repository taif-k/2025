import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import avatarImg from "../assets/images/avatar_img.PNG";

const RbImages = () => {
  const users = [
    { id: 1, name: "Radhika Parmar" },
    { id: 2, name: "Rajkumar Jadeja" },
  ];
  const avatarSizes = [20, 30, 40, 50, 60, 70];
  const groupCount = 5;

  return (
    <Container className="d-flex gap-6">

     
      <div>
        <p className="mb-2">Avatar With Name</p>
        <div className="d-flex gap-4">
          {users.map((user) => (
            <div key={user.id} className="d-flex align-items-center">
              <Image
                src={avatarImg}
                roundedCircle
                width={50}
                height={50}
                className="me-2"
              />
              <span>{user.name}</span>
            </div>
          ))}
        </div>
      </div>

    
      <div>
        <p className="mb-2">Avatar Sizes</p>
        <div className="d-flex gap-3 align-items-center flex-wrap">
          {avatarSizes.map((size, index) => (
            <Image
              key={index}
              src={avatarImg}
              roundedCircle
              width={size}
              height={size}
            />
          ))}
        </div>
      </div>

    
      <div>
        <p className="mb-2">Avatar Group</p>
        <div className="avatar-group d-flex align-items-center">
          {[...Array(groupCount)].map((_, index) => (
            <Image
              key={index}
              src={avatarImg}
              roundedCircle
              width={50}
              height={50}
            />
          ))}
        </div>
      </div>

    </Container>
  );
};

export default RbImages;
