// @ts-check
const { themes: prismThemes } = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AI Security Guide',
  tagline: 'Security for AI · AI for Security',
  favicon: 'img/favicon.ico',

  url: 'https://nabeelxy.github.io',
  baseUrl: '/ai-security-guide/',
  organizationName: 'nabeelxy',
  projectName: 'ai-security-guide',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',
  onBrokenAnchors: 'ignore',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: { defaultLocale: 'en', locales: ['en'] },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          // Read markdown from the repo root (one level up from site/)
          path: '..',
          routeBasePath: 'docs',
          sidebarPath: './sidebars.js',
          exclude: [
            // Docusaurus own files
            'site/**',
            // Downloaded papers & raw assets
            'raw/**',
            // Scripts
            'scripts/**',
            // Repo meta-files not meant for the public wiki
            'README.md',
            'CLAUDE.md',
            'LLM_WIKI_IDEA.md',
            '**/node_modules/**',
            '**/.git/**',
          ],
          editUrl:
            'https://github.com/nabeelxy/ai-security-guide/edit/main/',
          showLastUpdateTime: true,
        },
        blog: false,
        theme: { customCss: './src/css/custom.css' },
      }),
    ],
  ],

  plugins: [
    [
      '@easyops-cn/docusaurus-search-local',
      /** @type {import('@easyops-cn/docusaurus-search-local').PluginOptions} */
      ({
        hashed: true,
        indexDocs: true,
        indexBlog: false,
        docsRouteBasePath: '/docs',
        // Match the docs plugin's `path` setting (one level above site/)
        docsDir: '..',
        language: ['en'],
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
        searchResultLimits: 8,
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'AI Security Guide',
        logo: { alt: 'Shield', src: 'img/logo.svg' },
        hideOnScroll: true,
        items: [
          {
            label: 'Security for AI',
            to: '/docs/security_for_ai',
            position: 'left',
          },
          {
            label: 'AI for Security',
            to: '/docs/ai_for_security',
            position: 'left',
          },
          {
            label: 'AI Product Security',
            to: '/docs/ai_product_security',
            position: 'left',
          },
          {
            label: 'Offensive AI',
            to: '/docs/ai_for_offensive_security',
            position: 'left',
          },
          {
            label: 'AI Attacks in the Wild',
            to: '/docs/ai_powered_attacks',
            position: 'left',
          },
          {
            href: 'https://github.com/nabeelxy/ai-security-guide',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Security for AI',
            items: [
              { label: 'LLM Security', to: '/docs/security_for_ai/llm_security' },
              { label: 'Adversarial ML', to: '/docs/security_for_ai/adversarial_machine_learning' },
              { label: 'RAG Security', to: '/docs/security_for_ai/rag_security' },
              { label: 'Agent Security', to: '/docs/security_for_ai/agents_security' },
              { label: 'Red Teaming', to: '/docs/security_for_ai/red_teaming' },
            ],
          },
          {
            title: 'AI for Security',
            items: [
              { label: 'Web Security', to: '/docs/ai_for_security/web_security' },
              { label: 'Threat Intelligence', to: '/docs/ai_for_security/threat_hunting' },
              { label: 'Deepfakes', to: '/docs/ai_for_security/deepfakes' },
              { label: 'Binary Analysis', to: '/docs/ai_for_security/binary_analysis' },
            ],
          },
          {
            title: 'More',
            items: [
              { label: 'GitHub', href: 'https://github.com/nabeelxy/ai-security-guide' },
              {
                label: 'Cite This Guide',
                href: 'https://github.com/nabeelxy/ai-security-guide#citation',
              },
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} Mohamed Nabeel · CC BY 4.0 · Built with Docusaurus`,
      },
      prism: {
        theme: prismThemes.vsLight,
        darkTheme: prismThemes.vsDark,
        additionalLanguages: ['bash', 'python', 'json'],
      },
      tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 4,
      },
    }),
};

module.exports = config;
