import React from 'react';
import { Container, Row, Col} from 'react-bootstrap';

function Home() {
  return (
    <Container className="p-4">
      {/* Email UI */}
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h1>EmoAI Ethics Role-Play Activity</h1>
          <p>
            This website is developed as part of the student research to explore how role-playing help Emotion AI developers improve their awareness of ethical issues. Submitted answers will be used for research purposes only.
          </p>
        </Col>
      </Row>
      <Row>
        <Col>
          <h2>Guidelines and resources:</h2>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
