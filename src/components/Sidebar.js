import React from 'react';
import { Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <Nav className="flex-column p-3">
      <Nav.Link href="/" className="text-dark">EmoAI Ethics: Guidelines and Resouces</Nav.Link>
      <hr />
      <Nav.Link as={Link} to="/scenario1" className="text-dark">
        1 [Subject] — HR company
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario2" className="text-dark">
        2 [Subject] — Leading IT company
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario3" className="text-dark">
        3 [Subject] — Digital healthcare provider
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario4" className="text-dark">
        4 [Subject] — Video company
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario5" className="text-dark">
        5 [Subject] — School
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario6" className="text-dark">
        6 [Subject] — UX research team
      </Nav.Link>
    </Nav>
  );
}

export default Sidebar;
