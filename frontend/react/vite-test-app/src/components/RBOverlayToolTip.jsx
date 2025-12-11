import Button from 'react-bootstrap/Button';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';
import Popover from 'react-bootstrap/Popover';

const RBOverlayToolTip = () => {
  const placements = ['top', 'right', 'bottom', 'left'];

  return (
    <div className="d-flex flex-wrap gap-2">

      {placements.map((placement) => (
        <OverlayTrigger
          key={placement}
          trigger="click"
          placement={placement}
          overlay={
            <Popover id={`popover-${placement}`} className="grey-popover">
              <Popover.Header as="h3">{`Popover ${placement}`}</Popover.Header>
              <Popover.Body>
                This is a popover with <strong>grey text</strong>.
              </Popover.Body>
            </Popover>
          }
        >
          <Button variant="secondary">Popover on {placement}</Button>
        </OverlayTrigger>
      ))}


      <div className="d-flex gap-2 flex-wrap mt-2">
        {placements.map((placement) => (
          <OverlayTrigger
            key={placement}
            placement={placement}
            overlay={
              <Tooltip
                id={`tooltip-${placement}`}
                style={{
                  backgroundColor: 'white',
                  color: '#555',
                  border: '1px solid #ccc'
                }}
              >
                Tooltip on <strong>{placement}</strong>.
              </Tooltip>
            }
          >
            <Button variant="secondary">Tooltip on {placement}</Button>
          </OverlayTrigger>
        ))}
      </div>
    </div>
  );
};

export default RBOverlayToolTip;
