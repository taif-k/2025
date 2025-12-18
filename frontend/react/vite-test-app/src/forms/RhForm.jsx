import { useForm, Controller } from "react-hook-form";
import { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const RhForm = () => {
  const [loading, setLoading] = useState(false);
  const { control, register, handleSubmit, formState: { errors }, setError, watch, reset } = useForm();

  const hobbies = watch("hobby");
  const cities = watch("cities");
  const joiningDate = watch("joiningDate");

  const validateFile = (file, maxSize, allowedTypes) => {
    if (!file) return "File is required";
    if (file.size > maxSize) return "Max picture size - 6mb/ File size - 8bm  ";
    if (!allowedTypes.includes(file.type)) return "Invalid file type";
    return true;
  };

  const handleOnSubmit = (data) => {
    let hasError = false;

    if (!hobbies || hobbies.length < 2) {
      setError("hobby", { type: "manual", message: "Select at least 2 hobbies" });
      hasError = true;
    }

    if (!cities || cities.length < 2) {
      setError("cities", { type: "manual", message: "Select at least 2 cities" });
      hasError = true;
    }

    if (!joiningDate || joiningDate > new Date()) {
      setError("joiningDate", { type: "manual", message: "Select a past date" });
      hasError = true;
    }

    if (hasError) return false;

    setLoading(true);
    console.log("Submitting Form:", data);

    setTimeout(() => {
      alert("Form submitted");
      setLoading(false);
    }, 1500);

    console.log(JSON.stringify(data))
    reset()
  };

  // const formDetails = [
  //   {label: 'First Name', type: "text", regsiterArgument: 'firstname', reqMsg: 'First name required'},
  //   {label: 'Last Name', type: "text", regsiterArgument: 'lastname', reqMsg: 'Last name required'},
  //   {label: 'Age', type: "number", regsiterArgument: 'age', reqMsg: 'Age required'},]

  return (
    <Form onSubmit={handleSubmit(handleOnSubmit)}>
      <fieldset disabled={loading}>
        <Row>
          {/* first name */}
          <Col md={6}>
            <Form.Group className="mb-3" controlId="firstname">
              <Form.Label>First name</Form.Label>
              <Form.Control
                type="text"
                {...register("firstname", {
                  required: "First name is required.",
                  minLength: {
                    value: 2,
                    message: "First name must be at least 2 characters."
                  },
                  maxLength: {
                    value: 20,
                    message: "First name cannot exceed 20 characters."
                  },
                  pattern: {
                    value: /^[A-Za-z ]+$/,
                    message: "First name can only contain letters."
                  }
                })}
              />
              <div >{errors.firstname?.message}</div>
            </Form.Group>
          </Col>

          {/* last name */}
          <Col md={6}>
            <Form.Group className="mb-3" controlId="lastname">
              <Form.Label>Last name</Form.Label>
              <Form.Control
                type="text"
                {...register("lastname", {
                  required: "Last name is required.",
                  minLength: {
                    value: 2,
                    message: "Last name must be at least 2 characters."
                  },
                  maxLength: {
                    value: 20,
                    message: "Last name cannot exceed 20 characters."
                  },
                  pattern: {
                    value: /^[A-Za-z ]+$/,
                    message: "Last name can only contain letters."
                  }
                })}
              />
              <div >{errors.lastname?.message}</div>
            </Form.Group>
          </Col>
        </Row>

        <Row>
          {/* age */}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Age</Form.Label>
              <Form.Control
                type="number"
                {...register("age", {
                  required: "Age required",
                  min: { value: 18, message: "Min age 18" },
                  max: { value: 40, message: "Max age 40" },
                })}
              />
              <div >{errors.age?.message}</div>
            </Form.Group>
          </Col>

          {/* password */}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                {...register("password", {
                  required: "Password required",
                  minLength: { value: 6, message: "Min 6 characters" },
                  maxLength: { value: 10, message: "Max 10 characters" },
                })}
              />
              <div>{errors.password?.message}</div>
            </Form.Group>
          </Col>
        </Row>


        <Row>
          {/*phone */}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Phone Number</Form.Label>
              <Form.Control
                type="tel"
                {...register("phone", {
                  required: "Phone required", pattern: {
                    // value: /^[0-9]{10}$/,
                    value: /^(\+91|0)?[6-9]\d{9}$/,
                    message: "Enter 10 digit number(no space)",
                  },
                })}
              />
              <div>{errors.phone?.message}</div>
            </Form.Group>
          </Col>

          {/* email */}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                {...register("email", { required: "Email required" })}
              />
              <div>{errors.email?.message}</div>
            </Form.Group>
          </Col>
        </Row>


        <Row>
          {/* country */}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Country</Form.Label>
              <Form.Select {...register("country", { required: "Required" })}>
                <option value="">-- Select --</option>
                <option>India</option>
              </Form.Select>
              <div>{errors.country?.message}</div>
            </Form.Group>
          </Col>

          {/* state */}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>State</Form.Label>
              <Form.Select {...register("state", { required: "Required" })}>
                <option value="">-- Select --</option>
                <option>city 1</option>
              </Form.Select>
              <div>{errors.state?.message}</div>
            </Form.Group>
          </Col>
        </Row>

        {/* address*/}
        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Preferred Cities (min 2)</Form.Label>
              <Form.Select multiple {...register("cities")}>
                <option>abc</option>
                <option>def</option>
              </Form.Select>
              <div>{errors.cities?.message}</div>
            </Form.Group>
          </Col>

          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Address</Form.Label>
              <Form.Control
                as="textarea"
                rows={3}
                {...register("address", { required: "Address required" })}
              />
              <div>{errors.address?.message}</div>
            </Form.Group>
          </Col>
        </Row>


        <Row>
          {/* pin code*/}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Pincode</Form.Label>
              <Form.Control
                type="text"
                {...register("pincode", {
                  required: "Pincode required",
                  pattern: { value: /^[0-9]{6}$/, message: "6 digits required" },
                })}
              />
              <div>{errors.pincode?.message}</div>
            </Form.Group>
          </Col>

          {/* date*/}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Joining Date</Form.Label>
              <Controller
                control={control}
                name="joiningDate"
                render={({ field }) => (
                  <DatePicker
                    className="form-control"
                    placeholderText="Select Date"
                    selected={field.value}
                    onChange={field.onChange}
                    dateFormat="dd-MM-yyyy"
                  />
                )}
              />
              <div>{errors.joiningDate?.message}</div>
            </Form.Group>
          </Col>
        </Row>

        <Row>
          {/* gender*/}
          <Col md={6}>
            <Form.Group>
              <Form.Label>Gender</Form.Label>
              <div className="d-flex gap-3">
                {["Male", "Female", "Transgender"].map((g) => (
                  <Form.Check
                    key={g}
                    label={g}
                    type="radio"
                    value={g}
                    {...register("gender", { required: "Select gender" })}
                  />
                ))}
              </div>
              <div>{errors.gender?.message}</div>
            </Form.Group>
          </Col>

          {/* hobby*/}
          <Col md={6}>
            <Form.Group>
              <Form.Label>Hobbies (min 2)</Form.Label>
              <div className="d-flex gap-3 flex-wrap">
                {["Drawing", "Singing", "Dancing"].map((h) => (
                  <Form.Check key={h} label={h} type="checkbox" value={h} {...register("hobby")} />
                ))}
              </div>
              <div>{errors.hobby?.message}</div>
            </Form.Group>
          </Col>
        </Row>


        <Row className="mt-3">
          {/* profile picture*/}
          <Col md={6}>
            <Form.Group>
              <Form.Label>Profile Picture (Max 6MB)</Form.Label>
              <Form.Control
                type="file"
                accept="image/jpeg,image/png,image/gif"
                {...register("profile", {
                  validate: (fileList) =>
                    validateFile(
                      fileList?.[0],
                      6 * 1024 * 1024,
                      ["image/jpeg", "image/png", "image/gif"]
                    ),
                })}
              />
              <div>{errors.profile?.message}</div>
            </Form.Group>
          </Col>

          {/* resume*/}
          <Col md={6}>
            <Form.Group>
              <Form.Label>Resume (Max 8MB)</Form.Label>
              <Form.Control
                type="file"
                accept=".pdf,.doc,.docx"
                {...register("resume", {
                  validate: (fileList) =>
                    validateFile(fileList?.[0], 8 * 1024 * 1024, ["application/pdf", "application/msword",]),
                })}
              />
              <div>{errors.resume?.message}</div>
            </Form.Group>
          </Col>

          {/*Terms */}
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Check type="checkbox" label="Agree to terms and conditions"
                {...register("termandcondition", {
                  required: "Please accept the terms and conditions ",
                })}
              />
              <div >{errors.termandcondition?.message}</div>
            </Form.Group>
          </Col>
        </Row>
      </fieldset>

      <Button className="mt-4" type="submit" variant="primary" disabled={loading}>
        {loading ? "submitting form" : "Submit Form"}
      </Button>
    </Form>
  );
};

export default RhForm;
