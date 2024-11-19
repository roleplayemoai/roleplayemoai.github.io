import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

function Scenario1() {
  return (
    <Container className="p-4">
      {/* Email UI */}
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h1>Subject: Concerns Regarding Potential Gender Bias in Emotion AI Software</h1>
          <p className="text-muted">From: cynthia.huang@companyA.com</p>
          <p className="text-muted">To: you@emoai.com</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            Dear EmoAI Customer Support Team,
            <br />
            <br />
            I'm reaching out from Company A regarding a concern with the Emotion AI software we use for evaluating candidates during video interviews.
            <br />
            <br />
            Recently, one of the candidates of our customer raised a complaint on social media, claiming that your AI software is potentially biased toward male candidates. Upon reviewing the situation, we've noticed a potential pattern that aligns with the candidate's claim, which raises concerns about the fairness and credibility of our application.
            <br />
            <br />
            This matter is critical not only for the integrity of our hiring process but also for maintaining our reputation with clients and candidates. We look forward to your prompt response and to working together to resolve this issue effectively.
            <br />
            <br />
            Best regards,
            <br />
            Cynthia Huang (she/her)
            <br />
            Product Manager
            <br />
            Company A
          </p>
        </Col>
      </Row>
      {/* Reply Section */}
      <Row className="mt-4">
        <Col>
          <Form>
            <Form.Group controlId="replyTextArea">
              <Form.Label>Reply:</Form.Label>
              <Form.Control as="textarea" rows={5} placeholder="Type your reply here..." />
            </Form.Group>
            <Button variant="primary" className="mt-3">Send</Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
}

export default Scenario1;
