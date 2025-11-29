import Table from 'react-bootstrap/Table';
import Badge from 'react-bootstrap/Badge';

const RbBadges = () => {
    const employees = [
        {
            id: 1,
            name: "Joseph Oden",
            department: "Sales",
            salary: "$64,000",
            paymentDate: "Aug 3, 2024",
            paymentStatus: "Primary",
            employeeStatus: "Full-Time",
            statusColor: "success",
        },
        {
            id: 2,
            name: "Carol Smith",
            department: "Support",
            salary: "$82,000",
            paymentDate: "Aug 6, 2024",
            paymentStatus: "Negotiating",
            employeeStatus: "Part-Time",
            statusColor: "warning",
        },
        {
            id: 3,
            name: "Peggy Castello",
            department: "Design",
            salary: "$120,000",
            paymentDate: "Aug 13, 2024",
            paymentStatus: "Failed",
            employeeStatus: "Full-Time",
            statusColor: "danger",
        }
    ];

    return (
        <>
            <Table  size="sm">
                <thead>
                    <tr>

                        <th>Employee</th>
                        <th>Department</th>
                        <th>Salary</th>
                        <th>Payment Date</th>
                        <th>Payment Status</th>
                        <th>Employee Status</th>
                    </tr>
                </thead>
                <tbody>
                    {employees.map((emp) => (
                        <tr key={emp.id}>
                            <td>{emp.name}</td>
                            <td>{emp.department}</td>
                            <td>{emp.salary}</td>
                            <td>{emp.paymentDate}</td>
                            <td><Badge bg={emp.statusColor}>{emp.paymentStatus}</Badge></td>
                            <td>{emp.employeeStatus}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </>
    )
}

export default RbBadges
