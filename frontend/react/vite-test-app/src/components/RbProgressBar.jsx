import ProgressBar from 'react-bootstrap/ProgressBar';

const RbProgressBar = () => {
    const now = 60;
    return (
        <>
            <ProgressBar now={now} label={`${now}%`} />
        </>
    )
}

export default RbProgressBar
