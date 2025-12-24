import { Link, useParams } from 'react-router-dom'
import { ProductsData } from '../../data/product'
import { Badge, Image } from 'react-bootstrap'


const BlogDetail = () => {
  const param = useParams()
  const blogDetails = ProductsData.filter((product) => product.id === parseInt(param.id))
  // console.log((blogDetails[0]))
  return (
     <div>
      {/* <pre>{JSON.stringify(blogDetails, null, 2)}</pre> */}
      <Link to={'/blog'}>Back</Link>
      <Image src={blogDetails.thumbnail}></Image>
      <h1>Title: {blogDetails.title}</h1>
      <h1>Id: {blogDetails.id}</h1>
      <p>
          {blogDetails.body}
      </p>
      {/* {blogDetails?.tags?.map((tag, index)=>{
          return <Badge pill className='me-2' key={index}></Badge>
      })} */}
    </div>
  )
}

export default BlogDetail
