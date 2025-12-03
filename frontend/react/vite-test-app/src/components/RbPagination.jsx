import Pagination from 'react-bootstrap/Pagination';
import { useState } from 'react';

const RbPagination = () => {
  const [currentPage, setCurrentPage] = useState(12);

  const handleChange = (page) => {
    if (page !== 14) {
      setCurrentPage(page);
    }
  };

  return (
    <div>
      <p>Current page: {currentPage}</p>

      <Pagination>
        <Pagination.First onClick={() => setCurrentPage(1)} />
        <Pagination.Prev onClick={() => currentPage > 1 && setCurrentPage(currentPage - 1)} />

        <Pagination.Item
          active={currentPage === 1}
          onClick={() => handleChange(1)}
        >
          1
        </Pagination.Item>

        <Pagination.Ellipsis disabled />

        {[10, 11, 12, 13, 14].map((num) => (
          <Pagination.Item
            key={num}
            active={currentPage === num}
            disabled={num === 14}
            onClick={() => handleChange(num)}
          >
            {num}
          </Pagination.Item>
        ))}

        <Pagination.Ellipsis disabled />

        <Pagination.Item
          active={currentPage === 20}
          onClick={() => handleChange(20)}
        >
          20
        </Pagination.Item>

        <Pagination.Next onClick={() => currentPage < 20 && setCurrentPage(currentPage + 1)} />
        <Pagination.Last onClick={() => setCurrentPage(20)} />
      </Pagination>
    </div>
  );
};

export default RbPagination;
