import CloseButton from 'react-bootstrap/CloseButton';

const RbCloseButton = () => {
    return (
        <>
            <div data-bs-theme="dark" className='bg-dark p-2'>
                <CloseButton />
                <CloseButton disabled />
            </div>
        </>
    )
}

export default RbCloseButton
