/** @type {import('@docusaurus/types').Config} */
const math = require('remark-math');
const katex = require('rehype-katex');

const config = {
  title: 'SMARTHAUS Docs',
  tagline: 'Mathematics as the nervous system of AI',
  url: 'https://docs.smarthaus.ai',
  baseUrl: '/',
  organizationName: 'SmartHausGroup',
  projectName: '.github',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  i18n: { defaultLocale: 'en', locales: ['en'] },
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
      type: 'text/css',
    },
  ],
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/SmartHausGroup/.github/edit/main/',
          remarkPlugins: [math],
          rehypePlugins: [katex],
        },
        blog: false,
        theme: { customCss: require.resolve('./src/css/custom.css') },
      },
    ],
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */ ({
      navbar: {
        title: 'SMARTHAUS Docs',
        items: [
          { type: 'docSidebar', sidebarId: 'docs', position: 'left', label: 'Docs' },
          { href: 'https://www.smarthaus.ai', label: 'Website', position: 'right' },
          { href: 'https://github.com/SmartHausGroup/.github', label: 'GitHub', position: 'right' },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              { label: 'Intro', to: '/' },
              { label: 'About', to: '/about' },
              { label: 'Core Thesis', to: '/thesis/framework' },
              { label: 'RFS', to: '/rfs/overview' },
              { label: 'Methodology (MA)', to: '/mathematical-autopsy/overview' },
            ],
          },
          {
            title: 'Archetypes',
            items: [
              { label: 'TAI', to: '/archetypes/tai' },
              { label: 'AIVA', to: '/archetypes/aiva' },
              { label: 'MGE', to: '/archetypes/mge' },
            ],
          },
          {
            title: 'More',
            items: [
              { label: 'Website', href: 'https://www.smarthaus.ai' },
              { label: 'GitHub', href: 'https://github.com/SmartHausGroup/.github' },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} SmartHaus Group.`,
      },
      prism: { theme: require('prism-react-renderer/themes/github') },
    }),
};

module.exports = config;
