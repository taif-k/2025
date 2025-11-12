import React from 'react'

const UserStatus = ({ status = false }) => {
    return (
        <>
            <span className={`btn border-${status ? 'success' : 'danger'} text-${status ? 'success' : 'danger'}`}>
                {status ? "Online" : "Offline"}
            </span>
        </>
    )
}

export default UserStatus
