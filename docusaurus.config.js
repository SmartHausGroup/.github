/** @type {import('@docusaurus/types').Config} */
const math = require('remark-math');
const katex = require('rehype-katex');

const config = {
  title: 'SMARTHAUS',
  tagline: 'AI you can prove. Not AI you have to trust.',
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
        title: 'SMARTHAUS',
        items: [
          { type: 'doc', docId: 'six-failures', position: 'left', label: 'Why SMARTHAUS' },
          { type: 'doc', docId: 'products/ucp', position: 'left', label: 'Products' },
          { type: 'doc', docId: 'pali', position: 'left', label: 'PALI' },
          { type: 'doc', docId: 'mathematical-autopsy/overview', position: 'left', label: 'Methodology' },
          { type: 'doc', docId: 'research/princeton', position: 'left', label: 'Research' },
          { type: 'doc', docId: 'advisory/README', position: 'left', label: 'Advisory' },
          { href: 'https://smarthaus.ai', label: 'smarthaus.ai', position: 'right' },
          { href: 'https://github.com/SmartHausGroup', label: 'GitHub', position: 'right' },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Why SMARTHAUS',
            items: [
              { label: 'The Six Failures', to: '/six-failures' },
              { label: 'Mathematical Autopsy', to: '/mathematical-autopsy/overview' },
              { label: 'Math Thesis (v7)', to: '/thesis/framework' },
            ],
          },
          {
            title: 'Products',
            items: [
              { label: 'UCP — Universal Control Plane', to: '/products/ucp' },
              { label: 'SAID — Deterministic Inference', to: '/products/said' },
              { label: 'MAE — Mathematical Autopsy Engine', to: '/products/mae' },
              { label: 'PALI — Personal AI Layer', to: '/pali' },
            ],
          },
          {
            title: 'Research',
            items: [
              { label: 'Princeton Collaboration', to: '/research/princeton' },
              { label: 'Patents', to: '/research/patents' },
            ],
          },
          {
            title: 'More',
            items: [
              { label: 'Advisory', to: '/advisory' },
              { label: 'smarthaus.ai', href: 'https://smarthaus.ai' },
              { label: 'GitHub', href: 'https://github.com/SmartHausGroup' },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} SMARTHAUS Group.`,
      },
      prism: { theme: require('prism-react-renderer/themes/github') },
    }),
};

module.exports = config;
