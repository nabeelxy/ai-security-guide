import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

const SECTIONS = [
  {
    emoji: '🛡️',
    title: 'Security for AI',
    href: '/ai-security-guide/docs/security_for_ai',
    desc: 'LLM jailbreaks, prompt injection, poisoning, backdoors, adversarial ML, RAG security, agent attacks, MCP vulnerabilities, red teaming, and benchmarks.',
    meta: '9 topic areas · 100+ papers',
  },
  {
    emoji: '🔍',
    title: 'AI for Security',
    href: '/ai-security-guide/docs/ai_for_security',
    desc: 'AI-powered web security, DNS, IoT, threat hunting, enterprise cloud, deepfake detection, disinformation, email security, binary analysis, and more.',
    meta: '11 topic areas · 80+ papers',
  },
  {
    emoji: '🏗️',
    title: 'AI Product Security',
    href: '/ai-security-guide/docs/ai_product_security',
    desc: 'Engineering security into AI systems. Designing AI security detectors. ML security engineering practices for production.',
    meta: '2 topic areas',
  },
  {
    emoji: '⚔️',
    title: 'AI for Offensive Security',
    href: '/ai-security-guide/docs/ai_for_offensive_security',
    desc: 'Leveraging AI for ethical hacking, red teaming, vulnerability discovery, and penetration testing workflows.',
    meta: '1 topic area',
  },
  {
    emoji: '🌐',
    title: 'AI-Powered Attacks in the Wild',
    href: '/ai-security-guide/docs/ai_powered_attacks',
    desc: 'Tracking real-world AI-assisted attacks, campaigns, and incidents as they are reported and attributed.',
    meta: 'Continuously updated',
  },
];

const CITATION = `@misc{sai_ais,
  title  = {AI Security Guide: Security for AI and AI for Security},
  author = {Nabeel, Mohamed},
  howpublished = {\\url{https://github.com/nabeelxy/ai-security-guide}},
  year   = {2025}
}`;

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="A curated, continuously updated knowledge base on AI security — covering security vulnerabilities in AI systems and AI-powered defensive security."
    >
      <main>
        {/* ── Hero ───────────────────────────────────────────── */}
        <div className={styles.hero}>
          <h1 className={styles.heroTitle}>AI Security Guide</h1>
          <p className={styles.heroSubtitle}>
            A curated, continuously updated knowledge base covering{' '}
            <strong>Security for AI</strong> — threats, attacks, and defenses on
            AI systems — and <strong>AI for Security</strong> — using AI to
            enhance cyber defense.
          </p>
          <div className={styles.heroButtons}>
            <Link
              className="button button--primary button--lg"
              to="/ai-security-guide/docs/security_for_ai"
            >
              Browse the Guide
            </Link>
            <Link
              className="button button--secondary button--lg"
              href="https://github.com/nabeelxy/ai-security-guide"
            >
              GitHub
            </Link>
          </div>
          <div className={styles.stats}>
            <div className={styles.statItem}>
              <span className={styles.statNumber}>190+</span>
              <span className={styles.statLabel}>Papers tracked</span>
            </div>
            <div className={styles.statItem}>
              <span className={styles.statNumber}>20+</span>
              <span className={styles.statLabel}>Topic areas</span>
            </div>
            <div className={styles.statItem}>
              <span className={styles.statNumber}>40+</span>
              <span className={styles.statLabel}>Deep-dive reviews</span>
            </div>
            <div className={styles.statItem}>
              <span className={styles.statNumber}>800+</span>
              <span className={styles.statLabel}>Git commits</span>
            </div>
          </div>
        </div>

        {/* ── Section cards ──────────────────────────────────── */}
        <div className={styles.sectionsWrapper}>
          <h2 className={styles.sectionsTitle}>Explore by topic</h2>
          <div className={styles.sectionsGrid}>
            {SECTIONS.map((s) => (
              <Link key={s.title} to={s.href} className={styles.card}>
                <div className={styles.cardEmoji}>{s.emoji}</div>
                <div className={styles.cardTitle}>{s.title}</div>
                <div className={styles.cardDesc}>{s.desc}</div>
                <div className={styles.cardMeta}>{s.meta}</div>
              </Link>
            ))}
          </div>
        </div>

        {/* ── About ──────────────────────────────────────────── */}
        <div className={styles.about}>
          <h2>About</h2>
          <p>
            Prior to the ChatGPT moment, AI had already been enhancing security
            through threat detection and anomaly analysis. The proliferation of
            LLMs has accelerated this further — for the first time, defenders
            can crunch vast amounts of diverse, complex data at scale. But AI
            is itself one of the most vulnerable technologies ever built.
            Security for AI is paramount.
          </p>
          <p>
            This guide covers both directions: how AI systems can be attacked
            (jailbreaks, prompt injection, model poisoning, adversarial
            examples) and how AI can be used to defend (threat hunting, web
            security, binary analysis, deepfake detection). It is maintained as
            a living document, continuously updated with the latest research.
          </p>
          <h2>Citation</h2>
          <p>If you use this guide in your research, please cite:</p>
          <div className={styles.citationBlock}>{CITATION}</div>
        </div>
      </main>
    </Layout>
  );
}
