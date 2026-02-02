/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docs: [
    'intro',
    'thesis/framework',
    {
      type: 'category',
      label: 'Resonant Field Storage (RFS)',
      link: { type: 'doc', id: 'rfs/overview' },
      items: [
        'rfs/overview',
        'rfs/field-theory',
        {
          type: 'category',
          label: 'Use Cases',
          link: { type: 'doc', id: 'rfs/use-cases/overview' },
          items: [
            'rfs/use-cases/overview',
            'rfs/use-cases/incident-memory',
            'rfs/use-cases/rag-proofs',
            'rfs/use-cases/code-intelligence',
            'rfs/use-cases/compliance-legal',
            'rfs/use-cases/research-knowledge',
            'rfs/use-cases/pharmaceutical',
          ],
        },
      ],
    },
    'mathematical-autopsy/overview',
    {
      type: 'category',
      label: 'Archetypes',
      items: [
        'archetypes/tai',
        'archetypes/aiva',
        'archetypes/mge',
      ],
    },
    'about',
  ],
};

module.exports = sidebars;
