import { useContext } from 'react'
import { WishListContext } from '../context/Context'
import { Table, Button, Image, Row, Col } from 'react-bootstrap'

const WishList = () => {
  const { wishListState, wishListDispatch } = useContext(WishListContext)
  return (
    <Row>
      <Col>
        <Table bordered>
          {/* <thead>
            <tr>Products</tr>
          </thead> */}
          <tbody>
            {wishListState.wishlistItems.map((item, index) => {
              return (
                <tr key={index}>
                  <td>
                    <Image src={item.thumbnail} width={100} />
                    {item.title}
                  </td>
                  <td>
                    <Button 
                      size='sm'
                      variant='outline-danger' 
                      onClick={() => { wishListDispatch({ type: "REMOVE_FROM_WISHLIST", payload: item.id }) }}
                      >Remove</Button>
                  </td>
                </tr>
              )
            })}
          </tbody>
        </Table>
      </Col>
    </Row>

  )
}

export default WishList
