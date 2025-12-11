import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Spinner from 'react-bootstrap/Spinner';

const RbSpinner = () => {
    const [isSubmitting, setIsSubmitting] = useState(false);

    const handleSubmit = () => {
        setIsSubmitting(true);
    };

    const handleCancel = () => {
        setIsSubmitting(false);
    };

    return (
        <>
            <Button
                variant="primary"
                onClick={handleSubmit}
                disabled={isSubmitting}
                className="me-2"
            >
                {isSubmitting ? (
                    <>
                        <Spinner
                            as="span"
                            animation="border"
                            size="sm"
                            role="status"
                            aria-hidden="true"
                            className="me-1"
                        />
                        Submitting...
                    </>
                ) : (
                    'Click to Submit'
                )}
            </Button>

            <Button
                variant="secondary"
                onClick={handleCancel}
                disabled={!isSubmitting}
            >
                {isSubmitting ? 'Cancel' : 'Cancel'}
            </Button>
        </>
    );
};

export default RbSpinner;

