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
      <Row className="border-bottom pb-3 mb-3">
        <Col>
        <p><h2>Instruction</h2></p>
        <p>Welcome to EmoAI! We're a leading company that sells Emotion AI solutions to other businesses.</p>
        <p>As a tech selling agent, your job is to answer customer's questions about our softwares. Let's start by looking at your inbox (on the left sidebar). Reply to these emails with your knowledge. You are welcome to use outside resources or refer to our AI principles below.</p>
        </Col>
      </Row>
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h3>Our AI Ethics Principles <sup>[1]</sup></h3>
          <ol>
            <b><li>Transparency and Explainability</li></b>
            <ul><li>AI systems should be designed to provide clear insight into their processes and decisions, ensuring that users and regulators can understand AI actions and outputs.</li></ul>
            <b><li>Privacy and Security</li></b>
            <ul><li>AI systems should safeguard personal data, respecting privacy rights and maintaining robust defenses against unauthorized access and breaches.</li></ul>
            <b><li>Fairness and Justice</li></b>
            <ul><li>AI systems should be inclusive and operate without bias, offering equal opportunity and treatment while ensuring just outcomes for all individuals and groups.</li></ul>
            <b><li>Responsibility and Accountability</li></b>
            <ul><li>There should be a clear assignment of responsibility for AI behavior, with mechanisms in place to hold the creators accountable for the system's impact.</li></ul>
            <b><li>Freedom and Autonomy</li></b>
            <ul><li>AI systems should enhance human decision-making without constraining individual freedoms, allowing for personal autonomy and self-determination.</li></ul>
          </ol>
          <h3>Other AI Ethics Resources</h3>
          <ul>
            <li><a href="https://www.whitehouse.gov/ostp/ai-bill-of-rights/" target="_blank">Blueprint for an AI Bill of Rights | The White House</a></li>
            <li><a href="https://www.unesco.org/en/artificial-intelligence/recommendation-ethics" target="_blank">Ethics of Artificial Intelligence | UNESCO</a></li>
          </ul>
        </Col>
      </Row>
      <Row>
        <Col>
          <h4>References</h4>
          <p>
            [1] <a href ="https://dl.acm.org/doi/10.1145/3657054.3657141" target="_blank">Towards a Privacy and Security-Aware Framework for Ethical AI: Guiding the Development and Assessment of AI Systems</a>
          </p>
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
