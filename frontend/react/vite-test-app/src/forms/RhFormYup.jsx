import { useState } from "react";
import { Col, Form, Row } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import { useForm, Controller } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const schema = yup.object({
    firstname: yup.string().required("First name is required").matches(/^[A-Za-z ]+$/, "Only letters allowed").min(2, "Min 2 characters")
        .max(20, "Max 20 characters"),

    lastname: yup.string().required("Last name is required").matches(/^[A-Za-z ]+$/, "Only letters allowed").min(2, "Min 2 characters")
        .max(20, "Max 20 characters"),

    age: yup.number().typeError("Age must be a number").required("Age required").min(18, "Min age 18").max(40, "Max age 40"),

    password: yup.string().required("Password required").min(6, "Min 6 characters").max(10, "Max 10 characters")
        .test(
            "no-space",
            "Password should not contain spaces",
            value => !value?.includes(" ")
        ),

    phone: yup.string().required("Phone required").matches(/^(\+91|0)?\d{10}$/, "Invalid phone number"),

    email: yup.string().required("Email required").email("Invalid email"),

    country: yup.string().required("Country required"),

    state: yup.string().required("State required"),

    address: yup.string().required("Address required"),

    pincode: yup.string().required("Pincode required").matches(/^[0-9]{6}$/, "6 digits required"),

    gender: yup.string().required("Select gender"),

    hobby: yup.array().min(2, "Select at least 2 hobbies"),

    cities: yup.array().min(2, "Select at least 2 cities"),

    joiningDate: yup
        .date()
        .required("Joining date required")
        .test("previousDate", "Joining date must be before today", (value) => {
            if (!value) return false;

            const today = new Date();
            today.setHours(0, 0, 0, 0);

            const selectedDate = new Date(value);
            selectedDate.setHours(0, 0, 0, 0);

            return selectedDate < today;
        }
        )
    ,

    termandcondition: yup.boolean().oneOf([true], "Please accept terms and conditions"),

    profile: yup.mixed().required("Profile picture required").test("fileSize", "Max 6MB", file => file?.[0]?.size <= 6 * 1024 * 1024)
        .test(
            "fileType",
            "Invalid file type",
            file => ["image/jpeg", "image/png", "image/gif"].includes(file?.[0]?.type)
        ),

    resume: yup.mixed().required("Resume required")
        .test("fileSize", "Max 8MB", file => file?.[0]?.size <= 8 * 1024 * 1024)
});


const RhFormYup = () => {
    const [loading, setLoading] = useState(false);

    const { control, register, handleSubmit, formState: { errors }, reset } = useForm({
        resolver: yupResolver(schema),
        defaultValues: { hobby: [], cities: [] }
    });


    const handleRHFSubmit = (data) => {
        setLoading(true);
        console.log(data);

        setTimeout(() => {
            alert("Form submitted successfully!");
            setLoading(false);
            reset();
        }, 1500);
    };

    return (
        <Form onSubmit={handleSubmit(handleRHFSubmit)}>
            <fieldset disabled={loading}>
                {/*names */}
                <Row>
                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>First Name</Form.Label>
                            <Form.Control type="text" {...register("firstname")} />
                            <div className="text-danger">{errors.firstname?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Last Name</Form.Label>
                            <Form.Control type="text" {...register("lastname")} />
                            <div className="text-danger">{errors.lastname?.message}</div>
                        </Form.Group>
                    </Col>
                </Row>

                {/*age password */}
                <Row>
                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Age</Form.Label>
                            <Form.Control type="number" {...register("age")} />
                            <div className="text-danger">{errors.age?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="password" {...register("password")} />
                            <div className="text-danger">{errors.password?.message}</div>
                        </Form.Group>
                    </Col>
                </Row>

                  {/*phone email country address city */}
                <Row>
                    <Col md={6}>

                        <Form.Group className="mb-3">
                            <Form.Label>Phone</Form.Label>
                            <Form.Control type="tel" {...register("phone")} />
                            <div className="text-danger">{errors.phone?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Email</Form.Label>
                            <Form.Control type="email" {...register("email")} />
                            <div className="text-danger">{errors.email?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        {/* Country */}
                        <Form.Group className="mb-3">
                            <Form.Label>Country</Form.Label>
                            <Form.Select {...register("country")}>
                                <option value="">-- Select --</option>
                                <option value="India">India</option>
                            </Form.Select>
                            <div className="text-danger">{errors.country?.message}</div>
                        </Form.Group>
                    </Col>
                    <Col md={6}>
                        {/* State */}
                        <Form.Group className="mb-3">
                            <Form.Label>State</Form.Label>
                            <Form.Select {...register("state")}>
                                <option value="">-- Select --</option>
                                <option value="city1">city 1</option>
                            </Form.Select>
                            <div className="text-danger">{errors.state?.message}</div>
                        </Form.Group>
                    </Col>
                    <Col md={6}>
                        {/* Cities */}
                        <Form.Group className="mb-3">
                            <Form.Label>Preferred Cities (min 2)</Form.Label>
                            <Form.Select multiple {...register("cities")}>
                                <option value="abc">abc</option>
                                <option value="def">def</option>
                                <option value="def">ghi</option>
                            </Form.Select>
                            <div className="text-danger">{errors.cities?.message}</div>
                        </Form.Group>
                    </Col>
                    <Col md={6}>
                        {/* Address */}
                        <Form.Group className="mb-3">
                            <Form.Label>Address</Form.Label>
                            <Form.Control as="textarea" rows={3} {...register("address")} />
                            <div className="text-danger">{errors.address?.message}</div>
                        </Form.Group>
                    </Col>

                </Row>

                  {/*pin date */}
                <Row>
                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Pincode</Form.Label>
                            <Form.Control type="text" {...register("pincode")} />
                            <div className="text-danger">{errors.pincode?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Joining Date</Form.Label>
                            <Controller name="joiningDate" control={control} render={({ field }) => (
                                    <DatePicker className="form-control" selected={field.value} onChange={field.onChange} dateFormat="dd-MM-yyyy"/>
                                )}
                            />
                            <div className="text-danger">{errors.joiningDate?.message}</div>
                        </Form.Group>
                    </Col>
                </Row>

                  {/*gender hobby */}
                <Row >
                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Gender</Form.Label>
                            <div className="d-flex gap-3 flex-wrap">
                                {["Male", "Female", "Transgender"].map(g => (
                                    <Form.Check key={g} label={g} type="radio" value={g} {...register("gender")} />
                                ))}
                            </div>
                            <div className="text-danger">{errors.gender?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Hobbies (min 2)</Form.Label>
                            <div className="d-flex gap-3 flex-wrap">
                                {["Drawing", "Singing", "Dancing"].map(h => (
                                    <Form.Check key={h} label={h} type="checkbox" value={h} {...register("hobby")} />
                                ))}
                            </div>
                            <div className="text-danger">{errors.hobby?.message}</div>
                        </Form.Group>
                    </Col>
                </Row>

                  {/*resume picture t&c */}
                <Row className="mt-3">
                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Profile Picture</Form.Label>
                            <Form.Control type="file" {...register("profile")} />
                            <div className="text-danger">{errors.profile?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Label>Resume</Form.Label>
                            <Form.Control type="file" {...register("resume")} />
                            <div className="text-danger">{errors.resume?.message}</div>
                        </Form.Group>
                    </Col>

                    <Col md={6}>
                        <Form.Group className="mb-3">
                            <Form.Check
                                type="checkbox"
                                label="Agree to terms and conditions"
                                {...register("termandcondition")}
                            />
                            <div className="text-danger">{errors.termandcondition?.message}</div>
                        </Form.Group>
                    </Col>
                </Row>
            </fieldset>

            <Button className="mt-4" variant="primary" type="submit" disabled={loading}>
                {loading ? "submitting form" : "Submit"}
            </Button>
        </Form>

    );
};

export default RhFormYup;
